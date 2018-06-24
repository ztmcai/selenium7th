import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个csv文件，所以每次也应该关闭该文件

class CsvFileManager2:
    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file = open(path,'r')
        #通过csv代码库读取打开的csv文件,获取到文件中的数据集
        try:    #try尝试执行以下代码，
            data_table = csv.reader(file)
            a = [2,3,4,5,6]
            a[7] #这时可能会发生数据下标越界
            #如何保证，不论程序执行过程中是否报错，都能正常关闭该文件
            #for 循环 item每一个行 in 在数据集中 data_table表示数据集
            #data_table中有几行数据，我们就会执行几次
            for item in data_table:
                print(item)
            #方法最后应该添加close方法
        finally:   #finally最终，不论过程是否报错，都会执行以下代码

            file.close()
            print('file.close method is excuted')

#如果想测试一下这个方法
if __name__ == '__main__':
    csvr = CsvFileManager2()
    csvr.read()
#   如果在方法上面加上classmethod表示这个方法可以直接用类调用
#   如果在方法上写一个classmethod就不需要先实例化对象后才能调用
    #csvFileManager2.read()