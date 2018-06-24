import time
from selenium.webdriver import ActionChains

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这时 这个类不需要写setup teardown了
    #只需要写测试用例方法即可
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id('username').send_keys('cctest')
        driver.find_element_by_name('password').send_keys('cctest')
        old_title = driver.title
        driver.find_element_by_class_name('login_btn').click()
        time.sleep(5)
        new_title = driver.title
        #这是如果新标题和就标题不相等，就说明页面发生了跳转
        #如果相等就说明没有登录成功 页面没跳转
        print('旧页面'+old_title,'新页面'+new_title)
        self.assertNotEqual(old_title,new_title)


if __name__ == '__main__':
    unittest.main()