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

	def test_select_log(self):
		driver = self.driver
		driver.find_element_by_link_text(u"后台管理").click()
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		driver.find_element_by_link_text(u"管理日志").click()
		driver.find_element_by_id("name").send_keys(5)
		driver.find_element_by_xpath("html/body/div[1]/div[2]/div[2]/form/input[2]").submit()
		sleep(5)
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_select_log.jpg")
		driver.find_element_by_id("name").clear()
		driver.find_element_by_xpath("html/body/div[1]/div[2]/div[2]/form/input[2]").submit()
		sleep(5)
		driver.switch_to.window(windows[0])
		
	def test_select_case(self):
		driver = self.driver	
		driver.find_element_by_link_text("Case").click()
		driver.find_element_by_xpath(".//*[@id='BugFreeQuery_field1']/option[1]").click()
		driver.find_element_by_id("BugFreeQuery_value1").send_keys(10)
		driver.find_element_by_id("PostQuery").click()
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_select_case.jpg")
		

	def test_perform_case(self):
		driver = self.driver
		driver.find_element_by_link_text("Case").click()
		driver.find_element_by_xpath(".//*[@id='SearchResultDiv']/table/tbody/tr[1]/td[4]/span/a").click()
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		driver.find_element_by_xpath(".//*[@id='buttonlist']/input[3]").click()
		sleep(5)
		nowhandle = driver.current_window_handle
		allhandles = driver.window_handles
		for handle in allhandles:
			if handle != nowhandle:
				driver.switch_to.window(handle)		
		sleep(5)
		driver.find_element_by_xpath(".//*[@id='ResultInfoView_result_value']/option[2]").click()
		driver.find_element_by_id("ResultInfoView_mail_to").send_keys(u"系统管理员,")
		driver.find_element_by_id("Custom_OpenedBuild").send_keys("001")
		driver.find_element_by_xpath(".//*[@id='Custom_BugOS']/option[3]").click()
		driver.find_element_by_xpath(".//*[@id='Custom_BugBrowser']/option[6]").click()
		driver.find_element_by_xpath(".//*[@id='buttonlist']/input").click()
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_perform_case.jpg")
		driver.switch_to.window(windows[0])	

	def tearDown(self):
		driver = self.driver
		driver.find_element_by_link_text(u"退出").click()
		sleep(5)
		driver.quit()

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(Test("test_select_log"))
	suite.addTest(Test("test_select_case"))
	suite.addTest(Test("test_perform_case"))
	file = open("./test_result_%s.html"%(time.strftime("%Y-%m-%d %H-%M-%S")),"wb")
	runner = HTMLTestRunner(stream = file,title = u"bugfree测试报告",description = u"用例执行情况:")
	runner.run(suite)
	#runner = unittest.TextTestRunner()
	file.close()		







