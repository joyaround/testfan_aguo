#!/usr/bin/env python


import unittest
import HTMLTestRunner

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_upper(self):
        print("upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'], "yes, equals...")

    def tearDown(self):
        pass

def mysuite():
    testunit=unittest.TestSuite()
    testunit.addTest(TestStringMethods("test_upper"))
    testunit.addTest(TestStringMethods("test_isupper"))
    return testunit

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(mysuite())

    filename = 'TestfanResult1.html' #
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Testfan测试报告',
    description='用例执行情况：')
    runner.run(mysuite())