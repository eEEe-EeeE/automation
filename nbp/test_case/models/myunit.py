from selenium import webdriver
from .driver import browser
import unittest
import os


# 定义unittest单元测试
class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
