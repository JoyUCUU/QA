import unittest

from special_test_Android import unitestdemo

#针对单个测试用例
#mysuite = unittest.TestSuite()
#mysuite.addTest(unitestdemo.MyTestCase("testLoginFailed"))
#mysuite.addTest(unitestdemo.MyTestCase("testLoginOK"))

#针对一个测试类
cases = unittest.TestLoader().loadTestsFromTestCase(unitestdemo.MyTestCase)
mysuite = unittest.TestSuite([cases])
#也可直接添加单个测试用例
#mysuite.addTest(unitestdemo.MyTestCase("testLoginFailed"))
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)