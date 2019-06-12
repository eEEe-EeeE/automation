from selenium.webdriver.common.by import By
from .base_page import BasePage
from nbp.test_case.models import function
import time
import pyautogui
import pyperclip
import os


# 定期巡逻模块
class OmConfig(BasePage):

    # url : '/#/intelligent'

    def __init__(self, selenium_driver, base_url='http://192.168.1.23/#/'):
        super().__init__(selenium_driver, base_url)

    # XPath

    # 定位运维管理
    __om_loc = (By.XPATH, '//div/div[1]/ul[1]/li[4]/a')

    # 定位配置备份
    __om_config_loc = (By.XPATH, '//div/div[1]/ul[1]/li[4]/ul/li[6]/a')

    # 定位一级设备组
    __om_config_group_l1_loc = (By.XPATH, '//div/div[2]/div/div[1]/div[2]/ul/li/a')

    # 定位二级设备组
    __om_config_group_l2_loc = (By.XPATH, '//div/div[2]/div/div[1]/div[2]/ul/li/ul/li/a')

    # 定位设备
    __om_config_group_dev_loc = (By.XPATH, '//div/div[2]/div/div[1]/div[2]/ul/li/ul/li/ul/li/a')

    # 定位上传配置
    __om_config_upload_loc = (By.XPATH, '//div/div[2]/div/div[2]/div/div[1]/span[2]')

    # 定位版本号
    __om_config_upload_version_loc = (By.XPATH, '//div/div[2]/div/div[1]/div/div[2]/div/div[1]/input')

    # 定位版本说明
    __om_config_upload_explain_loc = (By.XPATH, '//div/div[2]/div/div[1]/div/div[2]/div/div[2]/textarea')

    # 定位选择文件
    __om_config_upload_select_loc = (By.XPATH, '//*[@id="FileUploader"]')

    # 定位开始上传
    __om_config_upload_confirm_loc = (By.XPATH, '//div/div[2]/div/div[1]/div/div[3]/form/button')

    # Locator

    def __om(self):
        return self.find_element(*self.__om_loc)

    def __om_config(self):
        return self.find_element(*self.__om_config_loc)

    def __om_config_group_l1(self):
        return self.find_elements(*self.__om_config_group_l1_loc)

    def __om_config_group_l2(self):
        return self.find_elements(*self.__om_config_group_l2_loc)

    def __om_config_dev(self):
        return self.find_elements(*self.__om_config_group_dev_loc)

    def __om_config_upload(self):
        return self.find_element(*self.__om_config_upload_loc)

    def __om_config_upload_version(self):
        return self.find_element(*self.__om_config_upload_version_loc)

    def __om_config_upload_explain(self):
        return self.find_element(*self.__om_config_upload_explain_loc)

    def __om_config_upload_select(self):
        return self.find_element(*self.__om_config_upload_select_loc)

    def __om_config_upload_confirm(self):
        return self.find_element(*self.__om_config_upload_confirm_loc)

    # Action

    def upload_config(self):
        time.sleep(1)
        self.__om().click()
        time.sleep(1)
        self.__om_config().click()
        time.sleep(1)

        # 输入数据是列表的列表，外层列表是所有行，内层列表是每一行的数据
        sheet_info = function.read_data(2)
        # 去掉表头
        sheet_info.pop(0)

        # 遍历xlsx的输入数据，填表单
        for input_row in sheet_info:

            # 根据xlsx的输入数据定位一级设备组
            g = self.__om_config_group_l1()
            g_l1 = {}
            for e in g:
                g_l1[e.text.split()[0]] = e

            # 找到输入项，并点击
            for n1, e1 in g_l1.items():
                if input_row[1] == n1:
                    e1.click()
                    break

            # 根据xlsx的输入数据定位二级设备组
            g = self.__om_config_group_l2()
            g_l2 = {}
            for e in g:
                g_l2[e.text.split()[0]] = e

            # 找到输入项，并点击
            time.sleep(1)
            for n2, e2 in g_l2.items():
                if input_row[2] == n2:
                    e2.click()
                    break

            file_name = function.ancestor_dir(3, __file__) + r'\\data\\' + input_row[5]
            file_name = file_name.replace(r'\\', '\\')
            # 为每个设备上传配置
            devs = self.__om_config_dev()
            for dev in devs:
                time.sleep(1)
                dev.click()
                self.__om_config_upload().click()
                self.__om_config_upload_version().send_keys(input_row[3])
                self.__om_config_upload_explain().send_keys(input_row[4])
                self.__om_config_upload_select().click()

                pyautogui.hotkey('altleft', 'N')
                pyperclip.copy(file_name)
                pyautogui.hotkey('ctrlleft', 'V')
                pyautogui.press('enter')
                self.__om_config_upload_confirm().click()

