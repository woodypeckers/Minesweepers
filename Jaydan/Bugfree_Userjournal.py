# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HTMLTestRunner import HTMLTestRunner


class Bugfree_Userjournal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/bugfree"
        self.driver = self.driver
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("LoginForm_username").clear()
        self.driver.find_element_by_id("LoginForm_username").send_keys("admin")
        self.driver.find_element_by_id("LoginForm_password").clear()
        self.driver.find_element_by_id("LoginForm_password").send_keys("111111")
        self.driver.find_element_by_id("LoginForm_rememberMe").click()
        self.driver.find_element_by_id("LoginForm_rememberMe").click()
        self.driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.find_element_by_link_text(u"退出").click()
        time.sleep(3)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_searchlog(self):
        '''后台管理-用户日志'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"后台管理").click()
        time.sleep(5)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.find_element_by_link_text(u"用户日志").click()
        driver.find_element_by_css_selector("input.btn").click()
        driver.find_element_by_xpath(u"//input[@value='重置查询']").click()
        driver.find_element_by_link_text("ID").click()
        driver.find_element_by_link_text(u"用户名").click()
        driver.find_element_by_link_text("IP").click()
        driver.find_element_by_link_text(u"登录时间").click()
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"上一页").click()
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_link_text(u"尾页").click()

    def test_trurname(self):
        '''后台管理-用户日志-查询日志'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"后台管理").click()
        time.sleep(5)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.find_element_by_link_text(u"用户日志").click()
        time.sleep(5)
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("12")
        driver.find_element_by_css_selector("input.btn").click()
        driver.find_element_by_link_text("ID").click()
        time.sleep(5)
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_link_text(u"用户名").click()
        time.sleep(5)
        driver.find_element_by_link_text("IP").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"登录时间").click()
        time.sleep(5)
        Select(driver.find_element_by_id("pageSize")).select_by_visible_text("35")
        Select(driver.find_element_by_id("pageSize")).select_by_visible_text("10")
        time.sleep(5)
        driver.switch_to.window(windows[0])

    def test_falsename(self):
        '''错误名称查询'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"后台管理").click()
        driver.find_element_by_link_text(u"用户日志").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("qwer")
        driver.find_element_by_css_selector("input.btn").click()
        driver.find_element_by_xpath(u"//input[@value='重置查询']").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("1000000")
        driver.find_element_by_css_selector("input.btn").click()
        driver.find_element_by_xpath(u"//input[@value='重置查询']").click()




if __name__ == "__main__":

    # unittest.TestSuite()

    suite = unittest.TestSuite()
    suite.addTest(Bugfree_Userjournal("test_searchlog"))
    suite.addTest(Bugfree_Userjournal("test_trurname"))
    suite.addTest(Bugfree_Userjournal("test_falsename"))
    file = open("./test_userlog_%s.html" % (time.strftime("%Y-%m-%d %H-%M-%S")), "wb")
    runner = HTMLTestRunner(stream=file, title=u"bugfree测试报告", description=u"用例执行情况:")
    runner.run(suite)
    # runner = unittest.TextTestRunner()
    file.close()