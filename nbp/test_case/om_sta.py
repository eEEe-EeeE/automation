from time import sleep
import unittest
import random
import sys
from nbp.test_case.models import myunit, function
from nbp.test_case.page_obj.login_page import Login
from nbp.test_case.page_obj.om_device_page import OmDevice
from nbp.test_case.page_obj.om_patrol_page import OmPatrol
from nbp.test_case.page_obj.om_config_page import OmConfig


class OmTest(myunit.MyTest):

    def user_login(self, username='sysadmin', password='123'):
        # 指定base_url时需要使用https，例如'https://10.10.3.9/#/'
        Login(self.driver).user_login(username, password)

    def om_device_verify(self):
        OmDevice(self.driver).insert_device()

    def om_patrol_verify(self):
        OmPatrol(self.driver).insert_task()

    def om_config_verify(self):
        OmConfig(self.driver).upload_config()

    def test_om(self):
        self.user_login()
        self.om_device_verify()
        # 应该加一些断言
        self.om_patrol_verify()
        # 应该加一些断言
        self.om_config_verify()
        # 应该加一些断言


if __name__ == '__main__':
    unittest.main()
