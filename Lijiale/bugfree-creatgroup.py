# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HTMLTestRunner import HTMLTestRunner

class BugfreeCreatgroup(unittest.TestCase):
    u"""测试用户管理组"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        driver = self.driver
        self.base_url = "http://localhost"
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.verificationErrors = []
        self.accept_next_alert = True
#后台管理-产品管理-复制
    def test_bugfree_houtaiguanli(self):
        u"""后台管理-产品管理-复制"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        all_handles = driver.window_handles
        driver.switch_to_window(all_handles[1])
        driver.find_element_by_link_text(u"复制").click()
        driver.find_element_by_id("Product_name").clear()
        driver.find_element_by_id("Product_name").send_keys(u"无卡商户11")
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("2")
        driver.find_element_by_id("Product_product_manager").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_css_selector("span").click()
        driver.find_element_by_css_selector("input.selectAll").click()
        driver.find_element_by_css_selector("label.selectAll.hover").click()
        driver.find_element_by_xpath(".//form[@id='product-form']/div[9]").click()
        driver.find_element_by_name("yt0").click()
        time.sleep(2)
#后台管理-用户管理-创建用户
    def test_bugfree_creatuser(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        all_handles = driver.window_handles
        driver.switch_to_window(all_handles[1])
        driver.find_element_by_link_text(u"用户管理").click()
        driver.find_element_by_link_text(u"添加用户").click()
        Select(driver.find_element_by_id("TestUser_authmode")).select_by_visible_text(u"内部帐号")
        driver.find_element_by_id("TestUser_username").clear()
        driver.find_element_by_id("TestUser_username").send_keys("lijiale2")
        driver.find_element_by_id("TestUser_realname").clear()
        driver.find_element_by_id("TestUser_realname").send_keys(u"黎家")
        driver.find_element_by_id("TestUser_password").clear()
        driver.find_element_by_id("TestUser_password").send_keys("123456")
        driver.find_element_by_id("TestUser_email").clear()
        driver.find_element_by_id("TestUser_email").send_keys("123456@qq.com")
        driver.find_element_by_name("yt0").click()
        time.sleep(2)
        #后台管理-用户组管理-添加用户组
    def test_bugfree_creatgroup(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=selenium_blank31171 | ]]
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_link_text(u"用户组管理").click()
        driver.find_element_by_link_text(u"添加用户组").click()
        driver.find_element_by_id("UserGroup_name").clear()
        driver.find_element_by_id("UserGroup_name").send_keys(u"信贷事业部1")
        driver.find_element_by_id("search_name").clear()
        driver.find_element_by_id("search_name").send_keys("admi")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=search_name_result | label=系统管理员[admin]]]
        driver.find_element_by_id("addUser").click()
        driver.find_element_by_id("search_name").clear()
        driver.find_element_by_id("search_name").send_keys("li")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=search_name_result | label=黎家[lijiale1]]]
        driver.find_element_by_id("addUser").click()
        driver.find_element_by_id("UserGroup_group_manager").click()
        driver.find_element_by_name("yt0").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # suite=unittest.TestSuite()
    # loader=unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromTestCase(BugfreeCreatgroup))
    # fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d-%H-%M-%S"),'wb')
    # runner = HTMLTestRunner(stream=fp,
    #                         title=u'后台管理-用户管理',
    #                         description=u'复制-用户创建-用户组创建')
    # runner.run(suite)
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器(套件)中
    testunit.addTest(unittest.makeSuite(BugfreeCreatgroup))   #baidu.Baidu中的baidu为用例所在的.py文件的名称，Baidu为测试用例集的名称
    #定义个报告存放路径，支持相对路径。
    filename= "C:\\Users\\lijiale\\Desktop\\selenium_element\\0625\\tijiao\\"+ u"测试报告正常" +"result.html"
    fp = open(filename,"wb")
    runner =HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    #执行测试用例
    runner.run(testunit)