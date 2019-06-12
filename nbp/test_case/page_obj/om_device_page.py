from selenium.webdriver.common.by import By
from .base_page import BasePage
from nbp.test_case.models import function
import time


# 运维管理模块
class OmDevice(BasePage):

    # url : '/#/intelligent'

    def __init__(self, selenium_driver, base_url='http://192.168.1.23/#/'):
        super().__init__(selenium_driver, base_url)

    # XPath

    # 定位运维管理
    __om_loc = (By.XPATH, '//div/div[1]/ul[1]/li[4]/a')

    # 定位设备管理
    __om_device_loc = (By.XPATH, '//div/div[1]/ul[1]/li[4]/ul/li[4]/a')

    # 定位一级设备组
    __om_device_group_l1_loc = (By.XPATH, '//div/div[2]/div/div[1]/div[2]/ul/li/a')

    # 定位二级设备组
    __om_device_group_l2_loc = (By.XPATH, '//div/div[2]/div/div[1]/div[2]/ul/li[1]/ul/li/a')

    # 定位设备列表，新增设备
    __om_device_list_loc = (By.XPATH, '//div/div[2]/div/div[2]/div[2]/ul/li[2]/a')
    __om_device_list_insert_loc = (By.XPATH, '//div/div[2]/div/div[2]/div[2]/ul/li[3]/span')
    __om_device_list_insert_confirm_loc = (By.XPATH, '//div/div[2]/div/div[2]/div[1]/div/div[3]/button')

    # 定位新增设备时需要添加的信息表单
    prefix1 = '//div/div[2]/div/div[2]/div[1]/div/div[2]/fieldset/div'
    __om_device_list_insert_info1_loc = [
        (By.XPATH, prefix1 + '[1]/input'),
        (By.XPATH, prefix1 + '[2]/select'),
        (By.XPATH, prefix1 + '[3]/select'),
        (By.XPATH, prefix1 + '[4]/select'),
        (By.XPATH, prefix1 + '[5]/input'),
        (By.XPATH, prefix1 + '[6]/input'),
        (By.XPATH, prefix1 + '[7]/input'),
        (By.XPATH, prefix1 + '[8]/select')
    ]

    # 定位第一个展开按钮
    __om_device_list_insert_switch1_loc = (
        By.XPATH, '//div/div[2]/div/div[2]/div[1]/div/div[2]/fieldset/div[9]/input'
    )

    # 第一个展开按钮下的表单
    prefix2 = '//div/div[2]/div/div[2]/div[1]/div/div[2]/div/fieldset/div'
    __om_device_list_insert_info2_loc = [
        (By.XPATH, prefix2 + '[1]/select'),
        (By.XPATH, prefix2 + '[2]/input'),
        (By.XPATH, prefix2 + '[3]/input'),
        (By.XPATH, prefix2 + '[4]/input'),
        (By.XPATH, prefix2 + '[5]/input'),
        (By.XPATH, prefix2 + '[6]/input')
    ]

    # 定位第二个展开按钮
    __om_device_list_insert_switch2_loc = (
        By.XPATH, '//div/div[2]/div/div[2]/div[1]/div/div[2]/div/fieldset/div[7]/input'
    )

    # 第二个展开按钮下的表单
    prefix3 = '//div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/fieldset/div'
    __om_device_list_insert_info3_loc = [
        (By.XPATH, prefix3 + '[1]/input'),
        (By.XPATH, prefix3 + '[2]/input'),
        (By.XPATH, prefix3 + '[3]/input')
    ]

    # 定位删除按钮
    __om_device_delete_loc = (By.XPATH, '//div/div[2]/div/div[2]/div[1]/div[2]/span[3]')

    # 定位删除确认按钮
    __om_device_delete_confirm_loc = (By.XPATH, '//div/div[2]/div/div[2]/div[1]/div/div[2]/div/span[1]')

    # Locator

    # 运维管理
    def __om(self):
        return self.find_element(*self.__om_loc)

    # 设备管理
    def __om_device(self):
        return self.find_element(*self.__om_device_loc)

    # 一级设备组
    def __om_device_group_l1(self):
        return self.find_elements(*self.__om_device_group_l1_loc)

    # 二级设备组
    def __om_device_group_l2(self):
        return self.find_elements(*self.__om_device_group_l2_loc)

    # 设备列表
    def __om_device_list(self):
        return self.find_element(*self.__om_device_list_loc)

    # 新增设备
    def __om_device_insert(self):
        return self.find_element(*self.__om_device_list_insert_loc)

    # 创建确定
    def __om_device_insert_confirm(self):
        return self.find_element(*self.__om_device_list_insert_confirm_loc)

    # 删除设备
    def __om_device_delete(self):
        return self.find_element(*self.__om_device_delete_loc)

    # 删除确定
    def __om_device_delete_confirm(self):
        return self.find_element(*self.__om_device_delete_confirm_loc)

    # Action

    def insert_device(self):
        time.sleep(1)
        self.__om().click()
        time.sleep(1)
        self.__om_device().click()
        time.sleep(1)

        # 输入数据是列表的列表，外层列表是所有行，内层列表是每一行的数据
        sheet_info = function.read_data(0)
        sheet_info.pop(0)

        # 遍历xlsx的输入数据，填表单
        for input_row in sheet_info:

            # 根据xlsx的输入数据定位一级设备组
            g = self.__om_device_group_l1()
            g_l1 = {}
            for e in g:
                g_l1[e.text.split()[0]] = e

            for n1, e1 in g_l1.items():
                if input_row[2] == n1:
                    e1.click()
                    break

            # 根据xlsx的输入数据定位二级设备组
            g = self.__om_device_group_l2()
            g_l2 = {}
            for e in g:
                g_l2[e.text.split()[0]] = e

            time.sleep(1)
            for n2, e2 in g_l2.items():
                if input_row[3] == n2:
                    e2.click()
                    break

            self.__om_device_list().click()
            self.__om_device_insert().click()

            # 调整输入表单长度
            input_len = 8

            info_loc = self.__om_device_list_insert_info1_loc

            s1 = self.find_element(*self.__om_device_list_insert_switch1_loc)
            if input_row[9] != 0:
                input_len += 6
                info_loc += self.__om_device_list_insert_info2_loc
                time.sleep(1)
                s1.click()
                s2 = self.find_elements(*self.__om_device_list_insert_switch2_loc)
                if input_row[16] != 0:
                    input_len += 3
                    info_loc += self.__om_device_list_insert_info3_loc
                    time.sleep(1)
                    s2.click()

            # 填参数
            for n in range(input_len):
                if n < 8:
                    self.find_element(*info_loc[n]).send_keys(input_row[n + 1])
                elif 8 <= n < 14:
                    self.find_element(*info_loc[n]).send_keys(input_row[n + 2])
                else:
                    self.find_element(*info_loc[n]).send_keys(input_row[n + 3])

            function.insert_img(self.driver, 'om_device_insert_before.png')

            # 确定
            self.__om_device_insert_confirm().click()

            function.insert_img(self.driver, 'om_device_insert_after.png')

            # 删除
            self.__om_device_delete().click()

            # 确定
            self.__om_device_delete_confirm().click()

            function.insert_img(self.driver, 'om_device_delete.png')

        time.sleep(1)

    # Assert

