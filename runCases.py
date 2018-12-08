#!/usr/bin/env python

import unittest
import HTMLTestRunner
from mytestcases import trybaidu
from mytestcases import tryTestfan

mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(trybaidu.Baidu))
mysuite.addTest(unittest.makeSuite(tryTestfan.Testfan))

filename = 'result2.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
#执行测试套件
# runner = unittest.TextTestRunner()
runner.run(mysuite)

# import unittest
# import HTMLTestRunner
#
# from OrganizedCases import trybaidu
# from OrganizedCases import tryTestfan
#
# testunit=unittest.TestSuite()
# #将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(trybaidu.Baidu))
# testunit.addTest(unittest.makeSuite(tryTestfan.Testfan))
# filename = 'c:\\workspace\\PySelenium\\result2.html'
# fp = open(filename, 'wb')
# runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
# #执行测试套件
# # runner = unittest.TextTestRunner()
# runner.run(testunit)