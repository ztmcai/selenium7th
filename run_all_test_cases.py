#这个文件是用来批量执行unittest的测试用例
#该文件是我们这个测试工具的唯一入口
#1.导入unittest，因为批量执行测试用例的功能由unittest代码库提供
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner

def send_mail(path):
    #1.通过path打开新生成的测试报告文件
    #html格式不是文本格式，需要指定以二进制方式打开
    file = open(path,'rb')
    #2.读取文件的内容,作为邮件正文
    msg = file.read()
    #3.把读取出来的内容转换成MIMEText的格式
    #电子邮件类型一般分三种：纯文本plain，html，多媒体（富文本）
    mime = MIMEText(msg, _subtype='html', _charset='utf-8')
    #4.除了正文以外，还需要设置主题，发件人，收件人
    mime['subject'] = '博为峰自动化测试报告'
    #发件人'bwftest126@126.com', 'abc123asd654'
    #因为发件人需要登录的客户端授权码
    #第三方登录不能直接用密码，必须用授权码
    mime['From'] = 'bwftest126@126.com'
    #收件人写自己的邮箱
    mime['To'] = 'ztmcai@163.com'

    #1.实现SMTP()构造方法
    smtp = smtplib.SMTP()
    #2.链接126邮箱服务
    smtp.connect('smtp.126.com')
    #3.登录126邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    #4.发送邮件
    smtp.send_message(mime, from_addr='bwftest126@126.com', to_addrs='ztmcai@163.com',)
    #5.退出
    smtp.quit()



if __name__ == '__main__':
    #2.要想批量执行，首先要明确你要执行哪些测试用例
    #只能执行继承了unittest.TestCase的类
    #比如执行这个项目中说有的unittest的测试用例
    #defaultTestLoader 是默认的测试用例加载器 可以用来发现所有的测试用例
    #*号表示通配符，可以代替任何字符
    #*Test.py表示已Test.py结尾的所有文件
    #.表示当前路径，即项目的根路径
    #suite随便起的变量名 suite本身是测试用例集的意思
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #suite = unittest.defaultTestLoader.discover('.', pattern='*.py')执行所有
    #3.找到测试用例后，执行这些测试用例
    #TextTestRunner()文本的测试用例运行器
    #unittest.TextTestRunner().run(suite)
    #4.生成测试报告HTMLTestRunner
    #HTMLTestRunner类似于TextTestRunner,都是批量执行测试用例的
    #区别在于，他们执行完所有测试用例的输出结果
    #一个是text，另一个是html
    #Text会被打印到控制台中 HTML会单独生成一个文件
    #相比于Text，HTML结构更清晰
    #所以二者选其一，用HTMLTestRunner代替TextTestRunner
    #我们需要把生成的测试报告保存到一个固定位置方便查看
    #在项目根节点下,创建一个文件夹 加report
    #以后生成的测试报告就保存在report下
    #5.定义测试报告的保存目录
    base_path = os.path.dirname(__file__)
    path = base_path + '/report/test_report2.html'
    #6.创建测试文件
    file = open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title='博为峰测试报告', description='测试环境:Server 2008;浏览器:Chrome').run(suite)
    #7.把测试报告作为邮件发送，好处是，可以起到及时提醒的作用
    #前提条件准备两个邮箱
    #版本控制的前提条件，申请一个git账号，并且邮箱激活
    #把html格式的测试报告，作为邮件正文发送
    send_mail(path)