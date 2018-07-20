#coding:utf-8
import time
import os
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '3DN4C16418006860'
desired_caps['appPackage'] = 'com.itiancai.finance.test'
desired_caps['appActivity'] = 'com.itiancai.finance.container.view.activity.SplashActivity_'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#安装同意界
#driver.find_element_by_id("com.android.packageinstaller:id/ok_button").click()
#点击界面的测试app
driver.find_elements_by_android_uiautomator('new UiSelector().text("甜菜金融(测试)")')
#等待20s，有默认询问页
time.sleep(5)
#跳过启动页
driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

#询问访问SDK
time.sleep(5)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
#再次询问
time.sleep(5)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
#进入我的页面
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
#填写手机号
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")').clear()
driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")').send_keys("13681267297")

#填写密码
time.sleep(5)
driver.find_elements_by_xpath('//android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText[1]').send_keys("qwe123")
#登陆
time.sleep(5)
driver.find_elements_by_xpath('//android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]').click()





