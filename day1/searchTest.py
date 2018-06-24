#1.打开主页
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://172.31.15.27:8081/')
#2.点击登录按钮

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/a[1]').click()
#3.输入iphone
#driver.find_element_by_name('keyword').send_keys('ipone')
#如果我们想在新的标签页上操作页面元素怎么办
#需要进行窗口切换
#driver.switch_to.window('第二个窗口名字')
#接下来的问题是如何获取第二个窗口的名字
#selenium提供了浏览器中所有窗口的名字的集合
#handle是句柄的意思，把句柄理解为名字就可以了
#driver.window_handles可以理解为是一个数组，我要求第二个窗口的名字
#[1]表示数组的第二个元素
#所以，第二个窗口名字即是 driver.window_handles[1]
#所以，窗口切换的语句就是：
driver.switch_to.window(driver.window_handles[1])
#这是再试一下 iphone会被输入到哪个搜索框中
driver.find_element_by_name('keyword').send_keys('ipone')
#这就是窗口切换方法
#[1]表示第二个元素，[-1]表示最后一个元素
#在python中元组和列表可以正着从0开始数
#也可以负着从-1开始数，倒数第一个-1 倒数第二个-2
#所以上面代码可以改成什么？把1改成-1试试
#如果这段代码能理解了，回到logintest点击加入购物车