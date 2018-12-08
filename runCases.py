#!/usr/bin/env python

import unittest
import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from time import sleep
from mytestcases import trybaidu
from mytestcases import tryTestfan


mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(trybaidu.Baidu))
mysuite.addTest(unittest.makeSuite(tryTestfan.Testfan))

reportfilename = 'result2.html'
fp = open(reportfilename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
runner.run(mysuite)
sleep(2)
exit()

smtpserver = 'smtp.163.com'
username = 'testfan_aguo@163.com'
password = 'testfan123'
sender = 'testfan_aguo@163.com'
# 收件人为多个收件人
receiver = ['joyaround@126.com', 'testfan_aguo@163.com']
subject = 'Python email test'

# 构造邮件对象MIMEMultipart对象
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'Testfan_AGuo@163.com <testfan_aguo@163.com>'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)
# msg['Date']='2012-3-16'

# 构造文字内容
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.testfan.cn"
text_plain = MIMEText(text, 'plain', 'utf-8')
msg.attach(text_plain)

# html = "test email"
# text_html = MIMEText(html, 'html', 'utf-8')
# text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
# msg.attach(text_html)

attachfile = "result2.html"
# 构造附件
sendfile = open(attachfile, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 附件可以重命名成aaa.txt，最好用原来文件名
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=attachfile)
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()