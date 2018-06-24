#这种框架的设计思想叫做page_object设计模式 是一种高级框架设计思想
#这种思想的主旨是把业务逻辑和代码技术分离开
#测试用例的类，专门负责业务逻辑
#元素定位和操作交给 网页对象
#在pageObject这个类中，把每个网页看成一个类
#网页中的每个元素看成类中的一个属性
#针对这个元素的操作看成类中的一个方法
#元素的信息，定位时名词性，所以可以看成属性（成员变量）
#元素的操作是动词性 所以可以看成是方法
#那么下面我们封装一下登陆这个网页

#这个类主要做的就是把元素定位改一个容易理解的名字

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    #为这个网页创建一个构造函数
    #在python中构造函数固定名字
    def __init__(self,driver):
        #因为setup方法中已经创建了一个浏览器 所以这里直接用setup创建好的
        #self.driver = webdriver.Chrome()
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"
    #声明一个变量username_input_loc，保存元素定位需要的两个参数
    #python 的元组类似于数组
    #这句话的意思是 声明了一个数组叫username_input_loc
    #这个数组中有两个元素 分别是By.ID 和 'username'
    username_input_loc = (By.ID,'username')
    password_input_loc = (By.ID,'password')
    login_button_loc = (By.CLASS_NAME,'login_btn')


    def open(self):
        self.driver.get(self.url)

    #给参数设置默认值 如果调用方法时 传入一个新的用户名 那么使用新的
    #如果调用方法时 不传参，那么使用默认值
    def input_uername(self,username='cctest'):
        #因为元素定位不太稳定 经常需要修改
        #所以应该把定位方式声明成类中的一个属性
        #*星号表示给find_element()传入的不是一个元组
        #而是把元组中的每个元素都分别传入find_element()方法，作为单独的参数
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password='cctest'):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

