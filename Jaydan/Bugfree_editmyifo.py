# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HTMLTestRunner import HTMLTestRunner

'''这个用例最后执行，否者会更改用户密码！！！'''
class Bugfree1(unittest.TestCase):


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
    
    def test_bugfree_editmyifo(self):
        '''编辑我的信息'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"编辑我的信息").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.find_element_by_id("TestUser_email").clear()
        driver.find_element_by_id("TestUser_email").send_keys("871138649@qq.com")
        driver.find_element_by_id("change_password").click()
        driver.find_element_by_id("TestUser_password_old").clear()
        driver.find_element_by_id("TestUser_password_old").send_keys("123456")
        driver.find_element_by_id("TestUser_password").clear()
        driver.find_element_by_id("TestUser_password").send_keys("111111")
        driver.find_element_by_id("TestUser_password_repeat").clear()
        driver.find_element_by_id("TestUser_password_repeat").send_keys("111111")
        Select(driver.find_element_by_id("TestUser_email_flag")).select_by_visible_text(u"是")
        driver.find_element_by_name("yt0").click()
        driver.switch_to.window(windows[0])
        time.sleep(5)

    def test_reports(self):
        '''统计报表'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Case").click()
        driver.find_element_by_link_text("Result").click()
        driver.find_element_by_link_text("Bug").click()
        driver.find_element_by_xpath('.//*[@id="VReport"]/a').click()
        driver.find_element_by_id("report3").click()
        driver.find_element_by_id("report4").click()
        driver.find_element_by_name("yt0").click()
        driver.find_element_by_link_text(u"统计报表").click()
        driver.find_element_by_id("report4").click()
        driver.find_element_by_id("report5").click()
        driver.find_element_by_id("report6").click()
        driver.find_element_by_id("select-all").click()
        driver.find_element_by_name("yt0").click()

    def test_BUG(self):
        '''查询BUG'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"我的标记").click()
        driver.find_element_by_css_selector("a.basic > span").click()
        driver.find_element_by_xpath("//div[@id='querymenu']/div[2]/ul/li[3]/a/span").click()
        driver.find_element_by_xpath("//div[@id='querymenu']/div[2]/ul/li[4]/a/span").click()


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Bugfree1("test_bugfree_editmyifo"))
    suite.addTest(Bugfree1("test_reports"))
    suite.addTest(Bugfree1("test_BUG"))
    file = open("./test_edimyifo_%s.html" % (time.strftime("%Y-%m-%d %H-%M-%S")), "wb")
    runner = HTMLTestRunner(stream=file, title=u"bugfree测试报告", description=u"用例执行情况:")
    runner.run(suite)
    # runner = unittest.TextTestRunner()
    file.close()