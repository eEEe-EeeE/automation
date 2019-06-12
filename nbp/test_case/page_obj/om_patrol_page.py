from selenium.webdriver.common.by import By
from .base_page import BasePage
from nbp.test_case.models import function
import time


# 定期巡逻模块
class OmPatrol(BasePage):

    # url : '/#/intelligent'

    def __init__(self, selenium_driver, base_url='http://192.168.1.23/#/'):
        super().__init__(selenium_driver, base_url)

    # XPath

    # 定位运维管理
    __om_loc = (By.XPATH, '//div/div[1]/ul[1]/li[4]/a')

    # 定位定期巡逻
    __om_patrol_loc = (By.XPATH, '//div/div[1]/ul[1]/li[4]/ul/li[5]/a')

    # 定位新建任务
    __om_patrol_create_task_loc = (By.XPATH, '//div/div[2]/div/div[2]/div[1]/span[2]')

    # 定位任务名称
    __om_patrol_name_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/input')

    # 定位任务类型
    __om_patrol_type_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/select')

    # 定位范围
    __om_patrol_range_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[3]/select')

    # 定位日历
    __om_patrol_calendar_loc = (By.XPATH, '//*[@id="RunTime"]')

    # prev
    __om_patrol_calendar_prev_loc = (By.XPATH, '//div[2]/div[2]/div[1]/table/thead/tr[1]/th[1]')

    # next
    __om_patrol_calendar_next_loc = (By.XPATH, '//div[2]/div[3]/div[1]/table/thead/tr[1]/th[3]')

    # left year and month
    __om_patrol_calendar_left_year_and_month_loc = (By.XPATH, '//div[2]/div[2]/div[1]/table/thead/tr[1]/th[2]')

    # right year and month
    __om_patrol_calendar_right_year_and_month_loc = (By.XPATH, '//div[2]/div[3]/div[1]/table/thead/tr[1]/th[2]')

    # left calendar
    __om_patrol_calendar_left_date_loc = (By.XPATH, '//div[2]/div[2]/div[1]/table/tbody//td')

    # right calendar
    __om_patrol_calendar_right_date_loc = (By.XPATH, '//div[2]/div[3]/div[1]/table/tbody//td')

    # left hour
    __om_patrol_calendar_left_hour_loc = (By.XPATH, '//div[2]/div[2]/div[2]/select[1]')

    # left minute
    __om_patrol_calendar_left_min_loc = (By.XPATH, '//div[2]/div[2]/div[2]/select[2]')

    # right hour
    __om_patrol_calendar_right_hour_loc = (By.XPATH, '//div[2]/div[3]/div[2]/select[1]')

    # right minute
    __om_patrol_calendar_right_min_loc = (By.XPATH, '//div[2]/div[3]/div[2]/select[2]')

    # confirm
    __om_patrol_calendar_confirm_loc = (By.XPATH, '//div[2]/div[4]/button[2]')

    # every day
    __om_patrol_cycle_day_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[5]/select')

    # every week
    __om_patrol_cycle_week_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[5]/select')

    # every month
    __om_patrol_cycle_month_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[5]/select')

    #

    # device list
    __om_patrol_device_list_loc = (
        By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[6]/div/div[1]/select/option'
    )

    # >
    __om_patrol_add_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[2]/div/div[6]/div/section/span[2]')

    # confirm
    __om_patrol_confirm_loc = (By.XPATH, '//div[1]/div[2]/div/div[1]/div/div[3]/button')

    # Locator
    def __om(self):
        return self.find_element(*self.__om_loc)

    def __om_patrol(self):
        return self.find_element(*self.__om_patrol_loc)

    def __om_patrol_create_task(self):
        return self.find_element(*self.__om_patrol_create_task_loc)

    def __om_patrol_name(self):
        return self.find_element(*self.__om_patrol_name_loc)

    def __om_patrol_type(self):
        return self.find_element(*self.__om_patrol_type_loc)

    def __om_patrol_range(self):
        return self.find_element(*self.__om_patrol_range_loc)

    def __om_patrol_calendar(self):
        return self.find_element(*self.__om_patrol_calendar_loc)

    def __om_patrol_calendar_prev(self):
        return self.find_element(*self.__om_patrol_calendar_prev_loc)

    def __om_patrol_calendar_next(self):
        return self.find_element(*self.__om_patrol_calendar_next_loc)

    def __om_patrol_calendar_left_year_and_month(self):
        return self.find_element(*self.__om_patrol_calendar_left_year_and_month_loc)

    def __om_patrol_calendar_right_year_and_month(self):
        return self.find_element(*self.__om_patrol_calendar_right_year_and_month_loc)

    def __om_patrol_calendar_left_date(self):
        return self.find_elements(*self.__om_patrol_calendar_left_date_loc)

    def __om_patrol_calendar_right_date(self):
        return self.find_elements(*self.__om_patrol_calendar_right_date_loc)

    def __om_patrol_calendar_left_hour(self):
        return self.find_element(*self.__om_patrol_calendar_left_hour_loc)

    def __om_patrol_calendar_left_min(self):
        return self.find_element(*self.__om_patrol_calendar_left_min_loc)

    def __om_patrol_calendar_right_hour(self):
        return self.find_element(*self.__om_patrol_calendar_right_hour_loc)

    def __om_patrol_calendar_right_min(self):
        return self.find_element(*self.__om_patrol_calendar_right_min_loc)

    def __om_patrol_calendar_confirm(self):
        return self.find_element(*self.__om_patrol_calendar_confirm_loc)

    def __om_patrol_cycle_day(self):
        return self.find_elements(*self.__om_patrol_cycle_day_loc)

    def __om_patrol_cycle_week(self):
        return self.find_elements(*self.__om_patrol_cycle_week_loc)

    def __om_patrol_cycle_month(self):
        return self.find_elements(*self.__om_patrol_cycle_month_loc)

    def __om_patrol_device_list(self):
        return self.find_elements(*self.__om_patrol_device_list_loc)

    def __om_patrol_add(self):
        return self.find_element(*self.__om_patrol_add_loc)

    def __om_patrol_confirm(self):
        return self.find_element(*self.__om_patrol_confirm_loc)

    # Action

    def insert_task(self):
        time.sleep(1)
        self.__om().click()
        self.__om_patrol().click()
        self.__om_patrol_create_task().click()

        # 输入数据是列表的列表，外层列表是所有行，内层列表是每一行的数据
        sheet_info = function.read_data(1)
        # 去掉表头
        sheet_info.pop(0)

        # 遍历xlsx的输入数据，填表单
        for input_row in sheet_info:
            self.__om_patrol_name().send_keys(input_row[1])
            self.__om_patrol_type().send_keys(input_row[2])
            self.__om_patrol_range().send_keys(input_row[3])

            # 当前年月日时分
            cur_datetime = time.strftime("%Y %m %d %H %M").split()
            before_offset_date = function.MyDate(int(cur_datetime[0]), int(cur_datetime[1]), int(cur_datetime[2]))

            # 调整偏移值 offset_day >= 0, 23 >= offset_hour >= 0, 59 >= offset_min >= 0x
            offset_day = input_row[4]
            offset_hour = input_row[5]
            offset_min = input_row[6]

            offset_hour += offset_min // 60
            offset_min = offset_min % 60

            offset_day += offset_hour // 24
            offset_hour = offset_hour % 24

            # 因为偏移天数为0时,偏移小时有限定
            if offset_day == 0 and offset_hour > 24 - (int(cur_datetime[3]) + 1):
                offset_day += 1
                offset_hour -= (24 - (int(cur_datetime[3]) + 1))

            # 偏移之后的年月日
            after_offset_date = before_offset_date + offset_day

            if input_row[3] == '选择范围':
                # 打开calendar面板
                self.__om_patrol_calendar().click()
                # 点击起始日期
                for i in range(42):
                    elements = self.__om_patrol_calendar_left_date()
                    if int(elements[i].get_attribute('textContent')) == before_offset_date.day:
                        elements[i].click()

                month_map = {
                    1: '一月',
                    2: '二月',
                    3: '三月',
                    4: '四月',
                    5: '五月',
                    6: '六月',
                    7: '七月',
                    8: '八月',
                    9: '九月',
                    10: '十月',
                    11: '十一月',
                    12: '十二月'
                }

                # 只点击左边的面板的日期，不符合条件就翻页
                # 获取左边面板的年份和月份
                left_year_and_month = \
                    self.__om_patrol_calendar_left_year_and_month().get_attribute('textContent').split()
                # 和输入年份，月份符合就点击
                while after_offset_date.year != int(left_year_and_month[1]) or \
                        month_map[after_offset_date.month] != left_year_and_month[0]:
                    self.__om_patrol_calendar_next().click()
                    left_year_and_month = \
                        self.__om_patrol_calendar_left_year_and_month().get_attribute('textContent').split()

                # 点击结束日期,先顺序索引再随机索引
                index = 0
                for i in range(42):
                    elements = self.__om_patrol_calendar_left_date()
                    if int(elements[i].get_attribute('textContent')) == 1:
                        index = i
                        break
                elements = self.__om_patrol_calendar_left_date()
                elements[index + after_offset_date.day - 1].click()

                self.__om_patrol_calendar_right_hour().send_keys(str(offset_hour).zfill(2))
                self.__om_patrol_calendar_right_min().send_keys(str(offset_min).zfill(2))
                self.__om_patrol_calendar_confirm().click()

            if input_row[7] == '每天':
                self.__om_patrol_cycle_day()[0].send_keys(input_row[7])
                self.__om_patrol_cycle_day()[1].send_keys(input_row[8].zfill(2))
            elif input_row[7] == '每周':
                self.__om_patrol_cycle_week()[0].send_keys(input_row[7])
                self.__om_patrol_cycle_week()[1].send_keys(input_row[8])
                self.__om_patrol_cycle_week()[2].send_keys(input_row[9].zfill(2))
            elif input_row[7] == '每月':
                self.__om_patrol_cycle_month()[0].send_keys(input_row[7])
                self.__om_patrol_cycle_month()[1].send_keys(input_row[8].zfill(2))
                self.__om_patrol_cycle_month()[2].send_keys(input_row[9].zfill(2))

            # 输入要加入设备的序号，从1开始
            d_input_list = input_row[10].split(',')
            d_list_len = len(self.__om_patrol_device_list())
            for i in d_input_list:
                i = int(i)
                if i <= d_list_len:
                    self.__om_patrol_device_list()[i - 1].click()
                    self.__om_patrol_add().click()

            self.__om_patrol_confirm().click()


