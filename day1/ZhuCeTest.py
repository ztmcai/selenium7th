from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://172.31.15.27:8081/index.php?m=user&c=public&a=reg')
driver.find_element_by_name('username').send_keys('cctest2')
driver.find_element_by_name('password').send_keys('cctest2')
driver.find_element_by_name('userpassword2').send_keys('cctest2')
driver.find_element_by_name('mobile_phone').send_keys('15211231234')
driver.find_element_by_name('email').send_keys('99999@qq.com')
driver.find_element_by_class_name('reg_btn').click()