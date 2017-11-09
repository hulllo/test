#!/usr/bin/env python3
# -*- coding: utf-8 -*-




__author__ = 'yuchuang.pan'
import sys

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def send_(emailsubject,emailcontent):
        ' a smtp send email module '
        ' emailsubject：邮件标题 '
        ' emailcontent：邮件内容 '
	# 输入Email地址和口令:
        from_addr = input('From: ')
        password = input('Password: ')
    # from_addr = input('输入用来发送邮件的邮箱地址（只支持outlook邮箱）'
    # password = input('输入邮箱密码')
    # 输入收件人地址:
        to_addr = input('To: ')
    #to_addr = 'hulllo@outlook.com'
    # 输入SMTP服务器地址:
    # smtp_server = input('SMTP server: ')
        smtp_server = 'smtp-mail.outlook.com'

        msg = MIMEText(emailcontent, 'html', 'utf-8')
        msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header(emailsubject, 'utf-8').encode()

    # smtp.starttls()
        server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
