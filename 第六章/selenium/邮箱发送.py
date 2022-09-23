# coding=gbk
"""
作者：川川
@时间  : 2021/11/10 10:50
群：970353786
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 写成了一个通用的函数接口，想直接用的话，把参数的注释去掉就好
def send_email(msg_from, passwd, msg_to, text_content, file_path=None):
    msg = MIMEMultipart()
    subject = "python 实现邮箱发送邮件"  # 主题
    text = MIMEText(text_content)
    msg.attach(text)


    if file_path:  # 最开始的函数参数我默认设置了None ，想添加附件，自行更改一下就好
        docFile = file_path
        docApart = MIMEApplication(open(docFile, 'rb').read())
        docApart.add_header('Content-Disposition', 'attachment', filename=docFile)
        msg.attach(docApart)
        print('发送附件！')
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()


msg_from = '28....579@qq.com'  # 发送方邮箱
passwd = 'dw....igrodhda'  # 填入发送方邮箱的授权码（就是刚刚你拿到的那个授权码）
msg_to = '28....9579@qq.com'  # 收件人邮箱，我是自己发给自己
text_content = "这是一个测试!"  # 发送的邮件内容
file_path = 'log.text'  # 需要发送的附件目录
send_email(msg_from, passwd, msg_to, text_content, file_path)
