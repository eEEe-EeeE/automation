import unittest
from nbp.test_case.models import myunit
from nbp.test_case.page_obj.login_page import Login
from nbp.test_case.page_obj.ca_show_page import CaShow


class CaTest(myunit.MyTest):

    def user_login(self, username='sysadmin', password='123'):
        # 指定base_url时需要使用https，例如'https://10.10.3.9/#/'
        Login(self.driver).user_login(username, password)

    def ca_show_verify(self):
        CaShow(self.driver).execute()

    def test_om(self):
        self.user_login()
        self.ca_show_verify()


if __name__ == '__main__':
    unittest.main()
