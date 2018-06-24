#1.导包
import unittest

import time
from selenium import webdriver

#2.继承unittest.TestCase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    #4.编写一个测试用例方法以test开头的方法
    def test_register(self):
        for row in CsvFileManager4().read('test_data.csv'):
            driver = self.driver
            driver.get('http://localhost/index.php?m=user&c=public&a=reg')
            #find_element(By.NAME,'username') == driver.find_element_by_name('username')
            #这两种方法没有任何区别 但是后面的这种方法扩展性更好 便于框架封装
            driver.find_element(By.NAME,'username').send_keys(row[0])
            driver.find_element(By.NAME,'password').send_keys(row[1])
            driver.find_element(By.NAME,'userpassword2').send_keys(row[2])
            driver.find_element(By.NAME,'mobile_phone').send_keys(row[3])
            driver.find_element(By.NAME,'email').send_keys(row[4])

            driver.find_element_by_name('username').submit()
            #在for循环中执行测试用例 虽然解决了批量执行的问题
            #但是，想想一下 如果第一行数据就报错了 那么后面还执行吗
            #考虑异常情况，输入完邮箱后 按tab键 检查提示信息是否都是通过信息验证
            #怎么验证 如果页面提示信息是通过信息验证 那么测试通过 否则测试失败
            check_tip = driver.find_element_by_css_selector('form.registerform.sign > ul > li:nth-child(1) > div > span').text
            print(check_tip)
            #其中check_tip是执行用例时，从网页上抓取的信息
            #通过信息验证 是来自于手工测试用例 是测试用例执行前的期望结果
            #if check_tip == '通过信息验证!':
                #print('测试通过')
            #else:
                #print('测试失败')
            #这样通过if...else语句 就可以自动判断测试用例的执行情况
            self.assertEqual('用户名不低于三位，使用中文、数字、字母皆可！',check_tip)
            #虽然第一行测试数据执行失败了 但是后面的测试数据是不依赖于前面的 不应该因为第一条失败就导致其他行数据不执行测试
            #所以我们不应该用for循环的方式执行不同的测试数据
            #因为在方法中写了for循环虽然执行了多次
            #但是unittest仍然认为他是一条测试用例，一旦断言失败就会终止这条测试用例
            #所以我们应该采用ddt框架实现数据驱动
if __name__ == '__main__':
    unittest.main()