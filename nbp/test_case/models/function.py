from selenium import webdriver
import os
import csv
import xlrd
import time
import datetime
import calendar


# 测试用例公用函数
# 向file_path目录插入截图
def insert_img(driver, file_name='test.png'):
    base_dir = ancestor_dir(3, __file__)
    file_path = base_dir + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)


# 从指定excel文件读取数据，第一个参数是表索引，第二个参数是文件路径
def read_data(sheet_index, file_name=r'.\nbp\data\input_data.xlsx'):
    # 打开文件file_name
    with xlrd.open_workbook(file_name, 'rb') as fp:
        # 读取某张表
        st = fp.sheet_by_index(sheet_index)
        rows_list = []
        # 过滤表
        for i in range(st.nrows):
            if i == 0:
                rows_list.append(st.row_values(i))
            else:
                # 过滤非第一行的所有数据，如果是float类型，则转换成int类型
                rows_list.append([n if not isinstance(n, float) else int(n) for n in st.row_values(i)])
    return rows_list


# 返回某个文件某个级别的目录
def ancestor_dir(level, module):
    parent_dir = os.path.dirname(module)
    for _ in range(level - 1):
        parent_dir = os.path.dirname(parent_dir)
    return parent_dir


class MyDate(object):

    # 每个月到1月1日的天数累加
    days_before_month = (
        0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365
    )

    def __init__(self, year, month=1, day=1):
        if isinstance(year, int) and year >= 1:
            self.__year = year
        if isinstance(month, int) and 1 <= month <= 12:
            self.__month = month
        if isinstance(day, int) and 1 <= day <= 31:
            self.__day = day
        years = self.__year - 1
        # 计算从公元1年1月1日开始到某个日期的总天数
        self.__total_days = 365 * years + \
            years // 4 - years // 100 + years // 400 + \
            self.days_before_month[self.__month - 1] + self.__day
        if self.is_leap_year(self.__year) and self.__month > 2:
            self.__total_days += 1

    def __add__(self, other):
        # 输入必须是整型
        if not isinstance(other, int):
            return self

        # 用累加法计算年号
        total_days = self.__total_days + other
        year = 1
        acc = 0
        while True:
            days_of_year = 366 if self.is_leap_year(year) else 365
            if acc + days_of_year >= total_days:
                break
            else:
                acc += days_of_year
                year += 1

        # rest 必定大于 0
        rest = total_days - acc
        # 累加法计算月号
        month = 1
        for v in self.days_before_month:
            if v < rest:
                month += 1
            else:
                month -= 1
                break
        # 最后易得天数
        day = rest - self.days_before_month[month - 1]
        return MyDate(year, month, day)

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__add__(-other)
        if isinstance(other, MyDate):
            return self.__total_days - other.__total_days

    # 类方法只能使用类属性，不能使用实例属性
    # 静态方法不能使用类属性，不能使用实例属性

    # 判断闰年
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    # 某个月的天数
    @staticmethod
    def days_of_month(year, month):
        if MyDate.is_leap_year(year):
            return (
                31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
            )[month - 1]
        else:
            return (
                31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
            )[month - 1]

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    @property
    def total_days(self):
        return self.__total_days


if __name__ == '__main__':
    result = read_data(1, r'..\..\data\input_data.xlsx')

