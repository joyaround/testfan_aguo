#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

driver = webdriver.Ie()
baseURL = "http://localhost:8040/"
driver.implicitly_wait(5)
driver.get(baseURL)
sleep(2)
number = random.randint(1,9999)
username = "testfan" + str(number)

# 1. 登录
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("imageField").click()
sleep(2)

# 2. 点击人员维护的菜单
driver.switch_to.frame("code")
driver.find_element_by_id("ri2").click()
sleep(2)

# 3.查询zhangsan8421
driver.switch_to.default_content()
driver.switch_to.frame("main")
driver.find_element_by_id("select-key:useruuid").send_keys("zhangsan8421")
driver.find_element_by_name("select-key_submit").click()
sleep(3)

# 4. 新增一个不存在的账号信息，账号做随机数处理
driver.find_element_by_name("record_record_addRecord").click()
#  切换到增加人员维护的窗口
#  切换到指定的窗口存在--遍历最多10次（String windowTitle）
signal = False
windows = driver.window_handles
driver.switch_to.window(windows[-1])
for i in range(10):
    windowsHandlers = driver.window_handles
    for h in windowsHandlers:
        driver.switch_to.window(h)
        title = driver.title
        if "增加人员维护" == title:
            signal = True
            break
    if signal: break
driver.find_element_by_id("record:useruuid").send_keys(username) # 之前定义的username
driver.find_element_by_id("record:name").send_keys("testfan")
driver.find_element_by_id("record:department").send_keys("测试部门")
s1 = driver.find_element_by_id("record:roleuuid")
Select(s1).select_by_visible_text("软件工程师--开发人员")
s2 = driver.find_element_by_id("record:ability")
Select(s2).select_by_value("000001")
driver.find_element_by_name("record_record_saveAndExit").click()

# 5.删除第4步新增的账号
#  切换到指定的窗口存在--遍历最多10次（String windowTitle）
signal = False
for i in range(10):
    windowsHandlers = driver.window_handles
    for h in windowsHandlers:
        driver.switch_to.window(h)
        title = driver.title
        if "软件应用框架" == title:
            signal = True
            break
    if signal: break

driver.switch_to.frame("main")
# 先在表格中搜索出这个账号
driver.find_element_by_id("select-key:useruuid").clear()
driver.find_element_by_id("select-key:useruuid").send_keys(username)
driver.find_element_by_name("select-key_submit").click()
driver.find_element_by_name("record:_flag").click()
sleep(5)
driver.find_element_by_name("record_record_deleteRecord").click() # 点击会触发alert的元素，比如按钮

sleep(5)
text1 = driver.switch_to.alert.text
driver.switch_to.alert.accept()
sleep(5)
alert2 = driver.switch_to.alert
text2 = alert2.text
alert2.accept()

driver.quit()