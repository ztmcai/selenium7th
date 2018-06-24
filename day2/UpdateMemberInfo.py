#1.登录海盗商城
#因为大部分测试用例都会用到登录功能，那么我们可不可以把登录功能单独封装成一个方法，每次直接调用这个方法就可以了
#这样，以后每次登录，就只需要用这个方法调用代码即可
import time
from selenium import webdriver

#文件名，类名，包名，都应该以字母开头，可以有数字和下划线
#但是不能有空格和中文
from day2.loginTest import Login

driver = webdriver.Chrome()
#每次创建浏览器时固定写一次，对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要检测页面的加载时间，监测什么时候页面加载完，什么时候执行后续的操作
driver.implicitly_wait(20)
#实例化对象会占用内存，pycharm会自动帮我们释放内存
#代码运行完，检测到Login（）这个对象，不再被使用，系统会自动释放内存
#把driver浏览器传入到登录方法中
#让登录方法和下面的点击账号设置使用同一个浏览器
#我们现在已经创建好一个空白的浏览器了，后续的所有操作都应该在这个浏览器上执行
Login().loginWithDefaultUser(driver)
#2.点击账号设置
#本来要点“账号设置”，需要使用driver这个变量但是现在文件中没有driver变量了
#可以重新声明一个driver么
driver.find_element_by_link_text('账号设置').click()
#3.点击个人资料
#partial_link_text可以使用链接一部分进行元素定位
#当链接文本过长时推荐使用partial_link_text
#使用partial_link_text方法时，可以用链接中的任意一部分，只要在网页中唯一即可
driver.find_element_by_link_text('个人资料').click()
#xpath方法比较通用 可以用工具自动生成，
#但是不推荐使用 作为一种没有办法时使用的方法
#因为xpath的可读性，和可维护性比较差
#4.修改真实姓名
#如果输入框中原本有内容，那么我们修改内容时，往往需要先清空原来的值，用clear（）方法
#实际上一个良好的编程习惯实在每次sendkeys之前，都应该先做clear操作
driver.find_element_by_id('true_name').clear()
driver.find_element_by_id('true_name').send_keys('测试测试')
#5.修改性别
#通过观察，可以发现，保密男，女，三者唯一的区别就是value属性的值不同
#那么我们可不可以通过value属性来定位
#可以，实际上我们可以通过任何属性来定位
#要想通过value属性来定位有两种方法：xpath和css_selector
#通过cssslector定位元素，只需要在唯一属性的两边加一对中括号即可
#driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中//表示采用相对路径定位元素
#/单斜杠表示绝对路径，一般都是从/html开始定位元素
#相对路径一般通过元素的特殊属性查找元素
#绝对路径一般通过元素的位置，层级关系查找元素
#绝对路径写起来比较长，涉及到节点比较多，当开发人员修改页面布局时，收到影响的可能性比较大
#相对路径，查询速度比较慢，因为可能需要遍历更多的节点
#工作中一般用绝对还是相对？工作中推荐用css_selector
#css_selector的查询速度比xpath快一点
#xpath在某些浏览器上支持的不太好，比如IE8
#css_selector所有前端开发都会用，便于沟通交流
#*表示任意节点
#[@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]').click()
#javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素
#然后下标选取其中的第n个元素，也可以用于定位，对不对？
#selenium可不可以用这种思路来定位元素
#要找页面上符合条件的所有元素就用find_elements这个方法
#要找页面上符合条件的唯一元素就用
driver.find_elements_by_id('xb')[2].click()
#6.修改生日
#一下一下电年月日是可以实现的
#但是稳定性比较差，很容易点错
#并且很难修改日期，比如写完1990-02-02下次想换个日期还需要从新去一个一个定位
#所以尽量不要用click（）点击选日期
#我们右键检查，可以发现日历控件其实是一个文本输入框
#那么我们可不可以用send_keys方法来输入一个日期
#日历控件明明是一个输入框，为什么不能输入？
#因为readonly属性，写一个javascript脚本，删除readonly属性
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id('date').clear()
driver.find_element_by_id('date').send_keys('1990-07-09')
#7.修改qq
driver.find_element_by_id('qq').clear()
driver.find_element_by_id('qq').send_keys('1233211314')
#8.点击确定，保存成功
driver.find_element_by_name('form1').submit()
time.sleep(3)
driver.switch_to.alert.accept()
