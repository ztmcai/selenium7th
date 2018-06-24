#用unittest写一个后台登陆的测试用例
#1.导包
import unittest

#2.建类，并集成unittest.TestCase
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUpClass(self):
        #做web自动化测试，是不是所有的测试用例都要先打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #窗口最大化代码，要求驱动版本必须和浏览器精准匹配
        self.driver.maximize_window()

    #4个空格，在pycharm中可以用tab键代替
    #对于初学者或者找工作的来讲 格式非常重要
    #算法是程序的灵魂，格式是程序的外表
    #外表是比灵魂重要的东西
    @classmethod
    def tearDownClass(self):
        #为了保证可以看清测试结果，可以在特爱人Down中价格30秒的延时等待
        time.sleep(10)
        #每次执行完测试用例，应该把打开的浏览器关闭
        #释放内 为下次执行测试用例做准备
        #这里调用的driver是声明在setUp方法中的一个局部变量
        #局部变量是不允许被其他方法访问的
        #所以我么你把setup中声明的driver改成一个全局变量
        #因为self表示类本身，所以我们只要在变量前加上self.就表示这个变量是属于类的
        self.driver.quit()

    def test_login(self):
        #因为每次使用driver变量时，都需要前面加一个self
        #为了简化代码，可以把成员变量的self.driver改写赋值给局部变量driver
        driver = self.driver
        driver.get('http://localhost/index.php?m=admin&c=public&a=login')
        driver.find_element_by_name('username').send_keys('admin')
        #有些常用的键也可以用转义字符代替，其中\t表示tab键 \n表示enter键
        ActionChains(driver).send_keys('\tpassword').send_keys('\t1234').send_keys('\n').perform()

    def test_product_adding(self):
        driver = self.driver
        #添加商品的代码
        #如果第二个方法重新打开一个浏览器，登录就无效了，怎么办？
        driver.find_element_by_link_text('商品管理').click()
        driver.find_element_by_link_text('添加商品').click()
        #除了用name属性切换frame也可以通过8种元素定位方法定位元素，然后切换
        iframe = driver.find_element_by_id('mainFrame')
        driver.switch_to.frame(iframe)
        #等于driver.switch_to.frame('mainFrame')
        driver.find_element_by_name('name').send_keys('饮水机')
        #变量名启明规则：数字 大写字母 下划线 一般要求以字母开头
        #如果id是纯数字用#号的方式不能定位
        #可以用[]的方式定位，所有的属性都可以用[]定位
        driver.find_element_by_id('1').click()
        driver.find_element_by_id('2').click()
        driver.find_element_by_id('6').click()
        #driver.find_element_by_id('7').click()
        ActionChains(driver).double_click(driver.find_element_by_id('7')).perform()
        select = Select(driver.find_element_by_name('brand_id'))
        select.select_by_value('1')
        driver.find_element_by_class_name('button_search').click()


if __name__ == '__main__':
    unittest.main()