#1.要想读取csv 首先要导入csv代码库
#csv不用下载 内置
#如果要读取excel需要下载响应代码库:xlrd
#怎么下载:1.通过命令下载：在dos窗口中，输入pip install -U xlrd
#selenium的离线包也可以通过命令行在线安装:
#pip install -U selenium 或者pip3 install selenium
#-U是升级到最新版的意思
#pip是python中的项目管理工具 和java中的maven类似
#如果你又安装python2同时安装python3，那么可能要把pip改成pip3
#点击File---settings---project interpreter---+
#搜索需要的代码库并可直接安装

import csv
#指定要读取的文件的路径
path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/test_data.csv'
#因为字符串中包含反斜线\t等，怎么办？
#1.每个反斜线前面加一个反斜线
#2.或者把每个反斜线都改成正的
#相比第二种方法更好一点，因为java python都是跨平台的语言
#在字符串中两个反斜线会自动转成一个反斜线
#在windows操作系统中，用反斜线\表示目录结构
#但是在linux操作系统中，只有正斜线/才能表示目录
#如果用反斜线就不能跨平台了因为linux用不了
#如果用正斜线 代码可以同时在linux windows中执行
#3.在字符串外面加上一个字母r，认为中间所有的代码都不存在转义字符
#print(path)

#3.打开路径所对应的文件
file = open(path,'r')
#4.读取文件的内容，通过什么来读取？我们是不是导入了csv代码库，还一直没用
#reader方法是专门用来读取数据文件的
data_table = csv.reader(file)

#5.打印data_table中的每一行数据 循环for-each语句
#for是循环关键字， item代表每一行，每循环一次就代表，item就代表最新的一行数据
#data_table表示整个文件中的所有数据
for item in data_table:
    print (item)
#我们是不是这样就成功从excel中读取出来所有的数据了
#很多的测试用例可能都需要从excel中读取数据，
#所以我们应该对这些代码做一个简单的封装,建一个文件叫csvfilemanager2,把以上代码封装到一个方法中
#并且再建一个文件去读取封装好的方法
