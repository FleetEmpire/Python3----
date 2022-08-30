#多变的参数传递
'''
我们在编程程序的时候对参数传递的要求是多种多样的，
python提供了多种传入参数的方法
1、位置参数：最普通的参数传递方式，形参和实参一一对应关系
2、关键字传参：为了避免参数传递出错，采用参数名=值得方式，
   而无需考虑参数的位置。
3、默认值传参：定义函数时，给形参设置默认值
4、可变参数：使用* 和** 表示，可传入多个参数，在调用的时候
就可以根据实际需要进行进行参数的传递。
一个*被自动组装为了元组，两个*被自动组装为了字典。

'''
#位置传参
'''
def max_num(a,b):
    if a > b:
        return a
    else:
        return b

m = max_num(12,5)
print(m)
'''

#关键字传参
'''
def max_num(a,b):
    if a > b:
        return a
    else:
        return b

m = max_num(b = 12,a = 5)
print(m)
'''


#默认值传参
'''
def max_num(b,a = 45):
    if a > b:
        return a
    else:
        return b

m = max_num(12)
print(m)
'''



#可变参数 *(自动组装元组)
'''
def animals(*name):
    print(name)
    print(type(name))
    str_name = ""
    for i in name:
        str_name += i
    return str_name


str = animals("小可爱","小航","小苹果","小豆豆")
print(str)
'''


#可变参数 **(自动组装字典)
def animals(**name):
    print(name)
    print(type(name))

animals(name1 = "小可爱",name2 = "小黄",name3 = "小苹果",name4 = "小豆")













































