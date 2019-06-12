import unittest
from nbp.test_case.models import myunit
from nbp.test_case.page_obj.login_page import Login
from nbp.test_case.models import function


class OmTest(myunit.MyTest):

    def user_login_verify(self, username='sysadmin', password='123'):
        Login(self.driver).user_login(username, password)

    def test_login(self):
        self.user_login_verify()
        lo = Login(self.driver)
        # 应该加入一些断言
        self.assertEqual(lo.user_login_success(), '网络边界安全巡逻系统')
        function.insert_img(self.driver, 'user_password_true.png')


if __name__ == '__main__':
    unittest.main()
