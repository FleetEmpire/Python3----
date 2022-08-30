#匿名函数
'''
优点：
使程序更加简洁；
省去函数命名烦恼；

缺点：
理解比较难；
函数体只是一个表达式，无法实现比较复杂的功能；

1.表达式中不能包含 循环，return

2.可以包含 if...else...语句.

3.表达式计算的结果直接返回

'''
#三元运算
'''
a = 12
b = 23
if a>b:
    print(a)
else:
    print(b)

a,b = 12,23
print(a) if a>b else print(b)
'''
#匿名函数
# 变量名= lambda 参数列表:表达式

func = lambda:1==3
f = func()
print(f)


func2 = lambda x,y,z:x+y+z
f = func2(12,34,10)
print(f)


func3 = lambda x,y:y if x > y else x
f = func3(12,34)
print(f)


















