from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://localhost/index.php?m=user&c=public&a=login')
driver.find_element_by_id('username').send_keys('cctest')
driver.find_element_by_name('password').send_keys('cctest')
driver.find_element_by_class_name('login_btn').click()
#点击链接 进入商城购物
#因为中间存在一个“登录成功”页面所以不能直接点击该链接
#解决办法三种方式：time.sleep ,隐式等待，显式等待
#WebDriverWait(driver,30,0.5).until(expected_conditions.)
WebDriverWait(driver,30,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,'进入商城购物')))
driver.find_element_by_link_text('进入商城购物').click()
#这句显示等待的代码，想到于time.sleep(20)的优化版代码