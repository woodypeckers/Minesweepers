#!/usr/bin/env python
#-*- coding:UTF-8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
class Test(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		driver = self.driver
		driver.implicitly_wait(30)
		self.base_url = "http://localhost/bugfree/index.php/site/login"

	def test_bugfree(self):
		driver = self.driver
		driver.get(self.base_url)
		nowhandle = driver.current_window_handle	
		driver.find_element_by_id("LoginForm_username").send_keys("admin")	
		driver.find_element_by_id("LoginForm_password").send_keys("123456")
		sleep(3)
		driver.find_element_by_id("LoginForm_rememberMe").click()
		driver.find_element_by_id("SubmitLoginBTN").click()
		driver.find_element_by_link_text(u" 新建 Bug   ").click()
		sleep(3)
		allhandles = driver.window_handles
		for handle in allhandles:
			if handle != nowhandle:
				driver.switch_to.window(handle)
				print driver.title
				driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div[1]/div[1]/input").send_keys("test_case001")
				sleep(3)
				driver.find_element_by_id("BugInfoView_assign_to_name").send_keys(u"系统管理员")
				driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/fieldset/div[4]/select/option[3]").click()
				driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/fieldset/div[6]/select/option[3]").click()
				driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/fieldset/div[7]/select/option[3]").click()	
				driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div[1]/fieldset[1]/div[3]/input").send_keys("test")
				driver.find_element_by_name("yt0").click()
				driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_bugfree.jpg")	
			if handle != nowhandle:
				driver.switch_to.window(nowhandle)
				sleep(3)  

	def test_add_product(self):
		driver = self.driver
		driver.get(self.base_url)
		nowhandle = driver.current_window_handle
		driver.find_element_by_id("LoginForm_username").send_keys("admin")	
		driver.find_element_by_id("LoginForm_password").send_keys("123456")
		driver.find_element_by_id("LoginForm_rememberMe").click()
		driver.find_element_by_id("SubmitLoginBTN").click()
		sleep(5)			
		driver.find_element_by_link_text(u"后台管理").click()	
		sleep(5)
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		sleep(3)
		driver.find_element_by_xpath("html/body/div[1]/div[2]/div[2]/form/a").click()
		sleep(5)
		driver.find_element_by_id("Product_name").send_keys("ql")
		sleep(3)
		driver.find_element_by_id("Product_display_order").send_keys("001")
		driver.find_element_by_id("Product_bug_severity").send_keys(1)
		driver.find_element_by_id("Product_bug_priority").send_keys(1)
		driver.find_element_by_id("Product_case_priority").send_keys(1)
		driver.find_element_by_xpath(".//*[@id='product-form']/input[2]").click()
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_add_product.jpg")
		driver.switch_to.window(windows[0])
	def test_case(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.find_element_by_id("LoginForm_username").send_keys("admin")	
		driver.find_element_by_id("LoginForm_password").send_keys("123456")
		driver.find_element_by_id("LoginForm_rememberMe").click()
		driver.find_element_by_id("SubmitLoginBTN").click()
		sleep(3)
		driver.find_element_by_link_text("Case").click()
		sleep(3)
		driver.find_element_by_xpath(".//*[@id='create_div']/a").click()
		sleep(3)
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		driver.find_element_by_id("CaseInfoView_title").send_keys("test")
		driver.find_element_by_id("CaseInfoView_assign_to_name").send_keys(u"系统管理员")
		driver.find_element_by_xpath(".//*[@id='CaseInfoView_priority']/option[2]").click()
		driver.find_element_by_xpath(".//*[@id='Custom_CaseType']/option[4]").click()
		driver.find_element_by_xpath(".//*[@id='Custom_CaseMethod']/option[2]").click()
		driver.find_element_by_xpath(".//*[@id='buttonlist']/input[1]").click()
		driver.get_screenshot_as_file("C:\\Users\\ming\\Desktop\\login\\test_case.jpg")
		driver.switch_to.window(windows[0])
	def tearDown(self):
		driver = self.driver
		driver.find_element_by_link_text(u"退出").click()
		driver.quit()

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(Test("test_bugfree"))
	suite.addTest(Test("test_add_product"))
	suite.addTest(Test("test_case"))
	file = open("./test_result_%s.html"%(time.strftime("%Y-%m-%d %H-%M-%S")),"wb")
	runner = HTMLTestRunner(stream = file,title = u"bugfree测试报告",description = u"用例执行情况:")
	runner.run(suite)
	#runner = unittest.TextTestRunner()
	file.close()
	#unittest.main()

