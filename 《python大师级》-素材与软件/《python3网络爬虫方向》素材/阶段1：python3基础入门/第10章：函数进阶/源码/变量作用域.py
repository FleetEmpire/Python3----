#python 变量与作用域
'''

1、局部 Local
   局部变量是定义在函数中的，因此其作用域是在函数内部。
   

2、全局 Global
和局部变量相对，全局变量是定义在函数外的变量，在全局都可以使用的变量。

3、global关键字


'''
#局部变量是定义在函数中的，因此其作用域是在函数内部。
'''
def func():
    a = 1
    print(a)

func()

'''


#全局变量 定义在函数外的变量，在全局都可以使用的变量。
'''
a = 12
def func():
    print(a+23)
print(a)
func()
'''


#当内部作用域想修改外部作用域的变量时，就要用到global关键字。
'''
a = 12
def func():
    global a
    a = 200
    print(a+23)
func()
print(a)
'''
num = 2
def sum(arg1,arg2):
    num = arg1+arg2
    print("这是局部变量："+str(num))
    return num
num = sum(23,56)
print(str(num)+"：是全局变量")



































































