# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HTMLTestRunner import  HTMLTestRunner

class BugfreeAdminLoginLogout(unittest.TestCase):
    u'''创建用例-查询用例-统计用例报表'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bugfree_admin_login_logout(self):
        u'''创建用例'''
        driver = self.driver
        driver.find_element_by_link_text(u" 新建 Bug   ").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | 新建Bug | ]]
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("BugInfoView_title").clear()
        driver.find_element_by_id("BugInfoView_title").send_keys("autotest002")
        driver.find_element_by_id("BugInfoView_assign_to_name").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_id("BugInfoView_mail_to").click()
        driver.find_element_by_xpath("//div[5]/ul/li").click()
        Select(driver.find_element_by_id("BugInfoView_severity")).select_by_visible_text("1")
        Select(driver.find_element_by_id("Custom_BugType")).select_by_visible_text(u"代码错误")
        Select(driver.find_element_by_id("Custom_HowFound")).select_by_visible_text(u"单元测试")
        driver.find_element_by_id("Custom_OpenedBuild").clear()
        driver.find_element_by_id("Custom_OpenedBuild").send_keys("001")
        driver.find_element_by_name("yt0").click()
        driver.close()
        
    def test_ide_bugfree_tongjibaobiao(self):
        u'''统计用例报表'''
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"统计报表").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | BugFree | ]]
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("select-all").click() 
        driver.find_element_by_name("yt0").click()
        driver.get_screenshot_as_file("E:\\tongjibaobiao.jpg")
        driver.close()
        
    def test_ide_bugfree_bugchaxun(self):
        u'''查询用例'''
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_css_selector("a.add_search_button > img").click()
        Select(driver.find_element_by_id("BugFreeQuery_field1")).select_by_visible_text(u"Bug标题")
        Select(driver.find_element_by_id("BugFreeQuery_operator1")).select_by_visible_text(u"包含")
        driver.find_element_by_id("BugFreeQuery_value1").clear()
        driver.find_element_by_id("BugFreeQuery_value1").send_keys("auto")
        driver.find_element_by_id("PostQuery").click()
        driver.find_element_by_css_selector("a.cancel_search_button > img").click()
        driver.find_element_by_id("PostQuery").click()
        driver.close()

    def tearDown(self):
        driver = self.driver
        self.driver.switch_to.window(driver.window_handles[0])
        self.driver.find_element_by_link_text(u"退出").click()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器(套件)中
    testunit.addTest(unittest.makeSuite(BugfreeAdminLoginLogout))   #baidu.Baidu中的baidu为用例所在的.py文件的名称，Baidu为测试用例集的名称
    #定义个报告存放路径，支持相对路径。
    filename= "C:\\Users\\lijiale\\Desktop\\selenium_element\\0625\\tijiao\\"+ u"测试报告正常" +"result.html"
    fp = open(filename,"wb")
    runner =HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    #执行测试用例
    runner.run(testunit)