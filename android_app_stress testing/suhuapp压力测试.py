#!/usr/bin/python
# -*- coding: UTF-8 -*-

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
#连接设备夜神模拟器
device = MonkeyRunner.waitForConnection(3,'127.0.0.1:62001')
#启动App
device.startActivity("com.sohu.sohuvideo/.FirstNavigationActivityGroup")
MonkeyRunner.sleep(2)
#点击搜索框
device.touch(200,180,'DOWN_AND_UP')
MonkeyRunner.sleep(1)
#输入查询词
device.type('tfboys')
MonkeyRunner.sleep(1)
#点击回车键
device.press('KEYCODE_ENTER','DOWN_AND_UP')
MonkeyRunner.sleep(1)
#点击搜索按钮
device.touch(850,100,'DOWN_AND_UP')
MonkeyRunner.sleep(6)
#截图
image = device.takeSnapshot()
image.writeToFile('./test.png','png')
#点击清除按钮
device.touch(750,100,'DOWN_AND_UP')
MonkeyRunner.sleep(3)

