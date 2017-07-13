# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HTMLTestRunner import HTMLTestRunner

class BugfreeHoutaiguanliChanpinguanli(unittest.TestCase):
    u"""后台管理"""
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
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bugfree_houtaiguanli_chanpinguanli(self):
        u"""产品管理-添加产品"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_link_text(u"添加产品").click()
        driver.find_element_by_id("Product_name").clear()
        driver.find_element_by_id("Product_name").send_keys(u"慧收银17")
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("8")
        #添加产品组、管理员
        # driver.find_element_by_css_selector("span").click()
        # driver.find_element_by_name("Product[group_name][]").click()
        # driver.find_element_by_css_selector("label.hover.checked").click()
        # driver.find_element_by_xpath("//form[@id='product-form']/div[9]").click()
        driver.find_element_by_id("Product_bug_severity").clear()
        driver.find_element_by_id("Product_bug_severity").send_keys("1,2,3,4,5")
        driver.find_element_by_id("Product_bug_priority").clear()
        driver.find_element_by_id("Product_bug_priority").send_keys("1,2,3")
        driver.find_element_by_id("Product_case_priority").clear()
        driver.find_element_by_id("Product_case_priority").send_keys("1,2,3")
        driver.find_element_by_name("yt0").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"慧")
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"慧收银")
        driver.find_element_by_css_selector("input.btn").click()
        driver.find_element_by_xpath(u"//input[@value='重置查询']").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"慧收银")
        driver.find_element_by_css_selector("input.btn").click()
    def test_bugfree_houtaiguanli_chanpinguanli_bianji(self):
        u"""产品管理-产品编辑"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[2]").click()
        driver.find_element_by_id("Product_product_manager").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_xpath("//a[@id='Product[group_name][]']/span").click()
        driver.find_element_by_css_selector("input.selectAll").click()
        driver.find_element_by_name("yt0").click()
    def test_bugfree_houtaiguanli_chanpinguanli_fuzhi(self):
        u"""产品管理-产品-复制-合并-模块"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_link_text(u"复制").click()
        driver.find_element_by_id("Product_name").clear()
        driver.find_element_by_id("Product_name").send_keys(u"好哒24")
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("1")
        driver.find_element_by_id("Product_product_manager").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_name("yt0").click()
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_link_text(u"合并").click()
        Select(driver.find_element_by_id("merge_dis_id")).select_by_visible_text(u"好哒")
        driver.find_element_by_name("yt0").click()
        # self.assertRegexpMatches(self.close_alert_and_get_its_text(), r'\'确定合并\'[\s\S]$')
        # time.sleep(3)
        # self.assertEqual(u"产品合并成功", self.close_alert_and_get_its_text())
        # time.sleep(3)
        driver.switch_to.alert.accept()  #接受弹出框   driver.switch_to.alert.dismiss() 取消
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.find_element_by_link_text(u"模块").click()
        driver.find_element_by_id("ProductModule_name").clear()
        driver.find_element_by_id("ProductModule_name").send_keys(u"慧收银商户")
        driver.find_element_by_id("ProductModule_add_owner_name").send_keys(u"系统管理员")
        #driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_id("ProductModule_display_order").clear()
        driver.find_element_by_id("ProductModule_display_order").send_keys("3")
        driver.find_element_by_name("yt0").click()
        driver.find_element_by_link_text(u"返回产品列表").click()
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
    #unittest.main()
    # testunit=unittest.TestSuite()
    # #将测试用例加入到测试容器(套件)中
    # testunit.addTest(unittest.makeSuite(BugfreeHoutaiguanliChanpinguanli))   #baidu.Baidu中的baidu为用例所在的.py文件的名称，Baidu为测试用例集的名称
    # #定义个报告存放路径，支持相对路径。
    # filename= "D:\\python\\report\\"+ u"测试报告正常" +"result.html"
    # fp = open(filename,"wb")
    # runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    # #执行测试用例
    # runner.run(testunit)
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(BugfreeHoutaiguanliChanpinguanli))
    fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d-%H-%M-%S"),'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'后台管理-用户管理',
                            description=u'复制-用户创建-用户组创建')
    runner.run(suite)