#usr/bin/python
#encoding:utf-8
import  time
from  appium import  webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.idainizhuang.dnz'
desired_caps['appActivity'] = 'com.idainizhuang.container.activity.SplashActivity'
print(desired_caps)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


time.sleep(3)
driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id("com.idainizhuang.dnz:id/mine_layout").click()

driver.find_element_by_id("com.idainizhuang.dnz:id/et_phone_number").send_keys("13312121212")
driver.find_element_by_id("com.idainizhuang.dnz:id/et_password").send_keys("jjjj1111")
driver.find_element_by_id("com.idainizhuang.dnz:id/btn_login").click()

try:
    if driver.find_element_by_id("com.idainizhuang.dnz:id/btn_login").is_displayed():
        print("fail")
except Exception as e:
    print(e)
    print("pass")

driver.quit()
time.sleep(5)

