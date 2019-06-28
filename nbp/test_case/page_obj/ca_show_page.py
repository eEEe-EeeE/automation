from selenium.webdriver.common.by import By
from .base_page import BasePage
from nbp.test_case.models import function
import time
import pyautogui
import pyperclip


#
class CaShow(BasePage):

    # url : '/#/intelligent'

    def __init__(self, selenium_driver, base_url='http://192.168.1.23/#/'):
        super().__init__(selenium_driver, base_url)

    # XPath

    #
    __ca_loc = (By.XPATH, '/html/body/div/div[1]/ul[1]/li[3]/a')

    #
    __ca_show_loc = (By.XPATH, '/html/body/div/div[1]/ul[1]/li[3]/ul/li[1]/a')

    #
    __ca_show_config_loc = (By.XPATH, '/html/body/div/div[2]/div/div/div[1]/ul/li[2]')

    #
    __ca_show_config_insert_loc = (By.XPATH, '/html/body/div/div[2]/div/div/div[1]/div/button')

    #
    __ca_show_config_edit_loc = (By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/span[1]/i')

    #
    __ca_show_config_insert_standard_loc = (By.XPATH, '//div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/input')

    #
    __ca_show_config_insert_items_loc = (By.XPATH, '//div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr')

    #
    __ca_show_config_insert_items_params_loc = (By.XPATH, './td/input | ./td/select')

    #
    __ca_show_config_insert_add_loc = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[2]/div/div[4]/span')

    #
    __ca_show_config_confirm_loc = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[3]/button')

    # Locator

    def __ca(self):
        return self.find_element(*self.__ca_loc)

    def __ca_show(self):
        return self.find_element(*self.__ca_show_loc)

    def __ca_show_config(self):
        return self.find_element(*self.__ca_show_config_loc)

    def __ca_show_config_insert(self):
        return self.find_element(*self.__ca_show_config_insert_loc)

    def __ca_show_config_edit(self):
        return self.find_element(*self.__ca_show_config_edit_loc)

    def __ca_show_config_insert_standard(self):
        return self.find_element(*self.__ca_show_config_insert_standard_loc)

    def __ca_show_config_insert_items(self):
        return self.find_elements(*self.__ca_show_config_insert_items_loc)

    def __ca_show_config_insert_add(self):
        return self.find_element(*self.__ca_show_config_insert_add_loc)

    def __ca_show_config_confirm(self):
        return self.find_element(*self.__ca_show_config_confirm_loc)

    # Action

    def execute(self):
        time.sleep(1)
        self.__ca().click()
        time.sleep(1)
        self.__ca_show().click()
        time.sleep(1)
        self.__ca_show_config().click()

        # 输入数据是列表的列表，外层列表是所有行，内层列表是每一行的数据
        sheet_info = function.read_data(
            0,
            r'C:\Users\someone\Documents\WeChat Files\c1505438001\FileStorage\File\2019-06\思科华为合规项.xlsx'
        )

        # 等保2.0
        time.sleep(1)
        self.__ca_show_config_edit().click()

        existing_item_num = len(self.__ca_show_config_insert_items())

        for _ in range(len(sheet_info)):
            self.__ca_show_config_insert_add().click()

        index = 0 + existing_item_num
        # 遍历xlsx的输入数据，填表单
        for input_row in sheet_info:
            items = self.__ca_show_config_insert_items()
            params = items[index].find_elements(*self.__ca_show_config_insert_items_params_loc)

            params[0].send_keys(input_row[0])
            params[1].send_keys(input_row[3][6:])
            params[2].send_keys('单行正则检测')
            params[3].send_keys('找到')
            params[4].send_keys('高')

            index += 1

        self.__ca_show_config_confirm().click()

        time.sleep(3)
