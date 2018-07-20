import unittest
from  appium import webdriver
import  time
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.idainizhuang.dnz'
        desired_caps['appActivity'] = 'com.idainizhuang.container.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetkeyboard'] = "True"
        print(desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    def testLoginOK(self):
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/mine_layout").click()
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/et_phone_number").send_keys("13312121212")
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/et_password").send_keys("jjjj1111")
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/btn_login").click()
        time.sleep(3)
        try:
            if self.driver.find_element_by_id("com.idainizhuang.dnz:id/btn_login").is_displayed():
                exist = True
        except Exception as e:
            exist = False
        self.assertEqual(exist, False)
    def testLoginFailed(self):
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/mine_layout").click()
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/et_phone_number").send_keys("11312121212")
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/et_password").send_keys("jjjj1111")
        self.driver.find_element_by_id("com.idainizhuang.dnz:id/btn_login").click()
        try:
            if self.driver.find_element_by_id("com.idainizhuang.dnz:id/btn_login").is_displayed():
                exist = True
        except Exception as e:
            exist = False
        self.assertEqual(exist, True)
    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()
