class BasePage(object):
    # 页面基础类，用于继承

    def __init__(self, selenium_driver, base_url, parent=None):
        self.driver = selenium_driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent

    # 根据指定url打开网页
    def _open(self, url):
        self.complete_url = self.base_url + url
        self.driver.get(self.complete_url)
        assert self.on_page(), 'Did not land on %s' % self.complete_url

    # 查找某个元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 查找多个元素
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 根据指定url打开网页
    def open(self, url=''):
        self._open(url)

    def on_page(self):
        return self.driver.current_url == self.complete_url

    def script(self, src):
        return self.driver.execute_script(src)

