#selenium执行javascript中的两个关键字:return(返回值) 和 arguments（参数）
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://172.31.15.27:8081/')
driver.implicitly_wait(20)
#点击登录链接
#用javascript方法找登录链接的代码：
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码：
#driver.find_element_by_link_text('登录')
#某些元素，用selenium的方法找元素比js更容易
#但是selenium不支持removeAttribute的方法
#但是selenium找到的登录链接和js找到的是同一个元素
#我们可不可以用selenium找到元素之后，转换成js元素
#这样以后写js就容易很多，不需要childNodes这些方法了
#比如，driver.find_element_by_link_text('登录').removeAttribute()
#driver.excute_script("document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute('target')")
login_link = driver.find_element_by_link_text("登录")
#把原来的js看成是一个无参无返的方法 现在直接从外面传入一个页面元素，就变成了一个有参无返的方法
#把selenium找到的这个元素 传入到javascript方法里 代替原来的js定位
#arguments参数的复数形式，[0]表示第一个参数，指的就是js后面的logi_link
#所以下面这句代码，相当于把driver.find_element_by_link_text('登录')带入到js语句中
#变成了driver.find_element_by_link_text('登录').removeAttribute('target')
#arguments是参数数组，指的是js字符串后面的所有参数
#一般情况下我们只会用到arguments[0]，即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#执行成功的自己写登录
driver.find_element_by_id('username').send_keys('cctest')
#driver.find_element_by_id('password').send_keys('cctest')
ActionChains(driver).send_keys(Keys.TAB).send_keys('cctest').send_keys(Keys.ENTER).perform()
#driver.find_element_by_id('username').submit()
#返回商城首页
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/span/a').click()
#搜索iphone
driver.find_element_by_name('keyword').send_keys('iphone')
driver.find_element_by_class_name('btn1').click()
#点击商品（用这种方法再实现一次不打开新窗口）
#product_link_xpath = "/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a"
product_link_css = 'body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a'
#使用js删除a标签的target属性
#通过xpath定位元素
#product_del = driver.find_element_by_xpath(product_link_xpath)
product_iphone = driver.find_element_by_css_selector(product_link_css)
#删除元素的target属性
driver.execute_script("arguments[0].removeAttribute('target')",product_iphone)
product_iphone.click()
#在商品详情页面点击加入购物车
driver.find_element_by_id('joinCarButton').click()
#driver.find_element_by_class_name('shopCar_T_span3').click()
driver.find_element_by_css_selector('.shopCar_T_span3').click()
#点击结算按钮
#在每个class前面都加一个小数点，并且去掉中间的空格，我们就可以同时用两个属性来定位一个元素
driver.find_element_by_css_selector('.shopCar_btn_03').click()
#点击添加新地址
driver.find_element_by_css_selector('.add-address').click()
#输入收货人等信息
driver.find_element_by_name('address[address_name]').send_keys('赵四')
driver.find_element_by_name('address[mobile]').send_keys('15019887654')
dropdown1 = driver.find_element_by_id('add-new-area-select')
#下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素专门创建了一个类Select
#dropdown1的类型是一个普通的网页元素，下面这句代码的意思是，
#把一个普通的网页元素，转换成一个下拉框的特殊网页元素
print(type(dropdown1))#dropdown1是webelement类型
#webelement这个类中只有click和send_keys这样的方法，没有选择下拉框选项的方法
select1 = Select(dropdown1)
print(type(select1))#select1是select类型
#转换成select类型之后，网页元素还是那个元素，但是select类中有选择选项的方法
#select1.select_by_value("320000")#这是我们就可以通过选项的值来定位了
time.sleep(2)
select1.select_by_visible_text("辽宁省")#也可以通过选项的文本信息来定位
#尝试一下选择沈阳
#因为是动态id所以不能通过id定位
#因为class重复所以我们不能直接用class定位
#但是我们可以用find_elements方法，先找到页面中所有class=add_new_area_select元素
#然后通过下标的方式选择第n个页面元素
#这种方法类似与以前学的js方法
dropdown2 = driver.find_elements_by_class_name('add-new-area-select')[1]
select2 = Select(dropdown2)
time.sleep(2)
select2.select_by_value('210100')

#dropdown3 = driver.find_elements_by_class_name('add-new-area-select')[2]等同于下面这句
#tag_name()这个方法，大多数情况都能找到一堆元素
#
dropdown3 = driver.find_elements_by_tag_name('select')[2]
select3 = Select(dropdown3)
time.sleep(2)
select3.select_by_visible_text('铁西区')

driver.find_element_by_name('address[address]').send_keys('一号楼1801')
driver.find_element_by_name('address[zipcode]').send_keys('100101')
driver.find_element_by_class_name('aui_state_highlight').click()
