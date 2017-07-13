# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from HTMLTestRunner import HTMLTestRunner


class Bugfree_Result(unittest.TestCase):
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

    def test_myflag(self):
        '''Result'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Result").click()
        driver.find_element_by_link_text(u"我的标记").click()
        Select(driver.find_element_by_id("BugFreeQuery_field1")).select_by_visible_text("ID")
        Select(driver.find_element_by_id("BugFreeQuery_operator1")).select_by_visible_text(u"不等于")
        driver.find_element_by_id("BugFreeQuery_value1").clear()
        driver.find_element_by_id("BugFreeQuery_value1").send_keys("1")
        Select(driver.find_element_by_id("BugFreeQuery_rightParenthesesName1")).select_by_visible_text(")")
        Select(driver.find_element_by_id("BugFreeQuery_leftParenthesesName1")).select_by_visible_text("(")
        Select(driver.find_element_by_id("BugFreeQuery_andor1")).select_by_visible_text(u"或者")
        driver.find_element_by_id("PostQuery").click()
        driver.find_element_by_id("SaveQuery").click()
        driver.find_element_by_id("dialogQueryTitle").clear()
        driver.find_element_by_id("dialogQueryTitle").send_keys(u"1我的标记")
        driver.find_element_by_name("yt0").click()

    def test_add(self):
        '''Result-增加查询'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//tr[@id='SearchConditionRow1']/td[7]/a/img").click()
        Select(driver.find_element_by_id("BugFreeQuery_field3")).select_by_visible_text(u"执行结果")
        Select(driver.find_element_by_id("BugFreeQuery_operator3")).select_by_visible_text(u"不等于")
        Select(driver.find_element_by_id("BugFreeQuery_value3")).select_by_visible_text("Passed")
        driver.find_element_by_id("PostQuery").click()
        driver.find_element_by_link_text(u"Result 标题").click()
        driver.find_element_by_link_text(u"创建者").click()
        driver.find_element_by_link_text(u"指派给").click()
        driver.find_element_by_link_text(u"相关 Case").click()
        driver.find_element_by_link_text(u"执行结果").click()
        driver.find_element_by_link_text(u"修改日期").click()

    def test_expetation(self):
        '''Result-自定义显示'''
        driver = self.driver
        driver.get(self.base_url )
        driver.find_element_by_id("CustomSetLink").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToSelectList | label=状态]]
        driver.find_element_by_id("addAllField").click()
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=fieldsToShowList | label=状态]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToShowList | label=抄送给]]
        driver.find_element_by_id("deleteAllField").click()
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=fieldsToSelectList | label=抄送给]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToSelectList | label=修改者]]
        driver.find_element_by_id("deleteField").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToSelectList | label=修改日期]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=fieldsToSelectList | label=修改者]]
        driver.find_element_by_id("addField").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToSelectList | label=指派给]]
        driver.find_element_by_id("addField").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToSelectList | label=执行结果]]
        driver.find_element_by_id("addField").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=fieldsToSelectList | label=抄送给]]
        driver.find_element_by_id("addField").click()
        driver.find_element_by_xpath(u"//input[@value='确定']").click()



if __name__ == "__main__":

    # unittest.TestSuite()

    suite = unittest.TestSuite()
    suite.addTest(Bugfree_Result("test_myflag"))
    suite.addTest(Bugfree_Result("test_add"))
    suite.addTest(Bugfree_Result("test_expetation"))
    file = open("./test_userlog_%s.html" % (time.strftime("%Y-%m-%d %H-%M-%S")), "wb")
    runner = HTMLTestRunner(stream=file, title=u"bugfree测试报告", description=u"用例执行情况:")
    runner.run(suite)
    # runner = unittest.TextTestRunner()
    file.close()