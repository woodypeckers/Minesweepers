#!/usr/bin/env python
#-*- coding:UTF-8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains

class Test(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		driver = self.driver
		driver.implicitly_wait(30)
		self.base_url = "http://localhost/bugfree/index.php/site/login"
		driver.get(self.base_url)
		driver.find_element_by_id("LoginForm_username").send_keys("admin")	
		driver.find_element_by_id("LoginForm_password").send_keys("123456")
		driver.find_element_by_id("LoginForm_rememberMe").click()
		driver.find_element_by_id("SubmitLoginBTN").click()
		sleep(5)

	def test_add_user(self):
		driver = self.driver
		driver.find_element_by_link_text(u"后台管理").click()
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		driver.find_element_by_link_text(u"用户管理").click()
		driver.find_element_by_link_text(u"添加用户").click()
		driver.find_element_by_xpath(".//*[@id='TestUser_authmode']/option[2]").click()
		driver.find_element_by_id("TestUser_username").send_keys("test_cache@123.com")
		driver.find_element_by_id("TestUser_realname").send_keys("wang")
		driver.find_element_by_id("TestUser_password").send_keys("123456")
		driver.find_element_by_id("TestUser_email").send_keys("test_cache@123.com")
		driver.find_element_by_xpath(".//*[@id='test-user-form']/input[2]").click()
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_add_user.jpg")
		driver.switch_to.window(windows[0])
		
	def test_add_user_group(self):
		driver = self.driver
		driver.find_element_by_link_text(u"后台管理").click()
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		driver.find_element_by_link_text(u"用户组管理").click()
		driver.find_element_by_link_text(u"添加用户组").click()
		driver.find_element_by_id("UserGroup_name").send_keys("group")
		driver.find_element_by_xpath(".//*[@id='search_name']").send_keys("admin")
		sleep(5)
		driver.find_element_by_xpath(".//*[@id='search_name_result']/option").click()
		sleep(3)
		#ActionChains(driver).move_to_element(admin).perform().click()
		driver.find_element_by_id("addUser").click()
		driver.find_element_by_id("UserGroup_group_manager").send_keys(u"系统管理员,")
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_add_user_group.jpg")
		driver.switch_to.window(windows[0])	

	def test_edit_system_set(self):
		driver = self.driver
		driver.find_element_by_link_text(u"后台管理").click()
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		driver.find_element_by_link_text(u"系统设置").click()
		driver.find_element_by_link_text(u"编辑").click()
		driver.find_element_by_id("TestOption_option_value").clear()
		driver.find_element_by_id("TestOption_option_value").send_keys(10)
		driver.find_element_by_xpath(".//*[@id='user-group-form']/input[2]").click()
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_edit_system_set.jpg")
		driver.switch_to.window(windows[0])	

	def tearDown(self):
		driver = self.driver
		driver.find_element_by_link_text(u"退出").click()
		driver.quit()

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(Test("test_add_user"))
	suite.addTest(Test("test_add_user_group"))
	suite.addTest(Test("test_edit_system_set"))
	#suite.addTest(Test("test_add_product"))
	#suite.addTest(Test("test_case"))
	file = open("./test_result_%s.html"%(time.strftime("%Y-%m-%d %H-%M-%S")),"wb")
	runner = HTMLTestRunner(stream = file,title = u"bugfree测试报告",description = u"用例执行情况:")
	runner.run(suite)
	#runner = unittest.TextTestRunner()
	file.close()		