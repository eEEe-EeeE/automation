from selenium.webdriver import Remote
from selenium import webdriver
import time


# 启动浏览器，使用selenium RC或者WebDriver
def browser():

    # 运行主机: 端口号，用于selenium RC
    host = '127.0.0.1:4444'

    # 指定浏览器，用于selenium RC
    dc = {'browserName': 'firefox'}

    driver = webdriver.Firefox()
    # driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)

    return driver

