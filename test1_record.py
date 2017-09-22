# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test1_record(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test1_record(self):
        success = True
        wd = self.wd
        wd.get("https://www.google.com.ua/?gws_rd=ssl")
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").clear()
        wd.find_element_by_id("lst-ib").send_keys("automation testing")
        wd.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
        wd.find_element_by_link_text("Test automation - Wikipedia").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
