#
#这个文件用来实现一个登录功能的自动化操作
#1.打开浏览器
import time
from selenium import webdriver
#从 谷歌公司的一个项目名 导入 网络驱动,用代码来操作浏览器
#http://npm.taobao.org/mirrors/chromedriver/ 下载最新谷歌驱动
driver = webdriver.Chrome()
#设置隐式等待：一旦找到页面元素，马上执行后面的语句
#如果超过20秒，仍然找不到页面元素，那么程序将会报错
driver.implicitly_wait(20)
#2.打开海盗商城主页
#driver.get('http://172.31.15.27:8081/')
#3.打开登陆页面
driver.get('http://172.31.15.27:8081/index.php?m=user&c=public&a=login')
#4.输入用户名密码
driver.find_element_by_id('username').send_keys('cctest')
driver.find_element_by_name('password').send_keys('cctest')
#5.点击登陆按钮
#所有调用方法都会有提示信息，没有提示信息就说明没有这个方法
driver.find_element_by_class_name('login_btn').click()
#6.检查登陆是否成功,按照现在所学还不能定位用户名信息，稍后在考虑这个问题
#现在自己实现一个自动化注册功能
#Alt + Enter 导包快捷键，选import this name，选最短的time
#time.sleep()这个方法提供了一种固定的时间等待，
#这里的意义是点击登录按钮后，等5秒后在检查用户名是否正常显示
#弊端是，因为网络延迟不知道每次等1秒合适还是等5秒合适
#解决办法：使用智能等待替换固定等待
#time.sleep(5)
username_text = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/a[1]').text
#print(username_text)
#我们可以通过if语句判断页面显示的文本和预期的文本和预期的文本是否一致，来判断测试用例是否正常执行
#if username_text == '您好 cctest'
   # print('测试执行通过')
#else:
    #print('测试执行失败')
#因为selenium主要做回归测试,所以测试脚本刚开始都是pass的，只有开发做了代码变更，我们的测试用例才有可能失败
#一般工作中不用if else语句做判断 后面再详细讨论这个问题
#7.点击“进入商城购物”
#driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a').click()
#xpath有一个缺点，定位元素可读性比较差，有没有可读性好一点的方法
driver.find_element_by_link_text('进入商城购物').click()
#8.在商城主页输入搜索条件ipone
#time.sleep(2)
driver.find_element_by_name('keyword').send_keys('iphone')
#9.点击搜索按钮
driver.find_element_by_class_name('btn1').click()
#10.在搜索结果页面 点击第一个商品的图片
#time.sleep(3)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img').click()
#time.sleep(3)
#serach_window = driver.current_window_handle
#time.sleep(5)
#窗口切换
driver.close() #关闭selenium正在运行的窗口
driver.switch_to.window(driver.window_handles[-1])
#11.点击加入购物车
driver.find_element_by_id('joinCarButton').click()