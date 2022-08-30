#比较运算符
'''
运算符 描述 示例代码 
== 恒等，表示对象是否相等，和=是不一样的 a == b 返回值为Fasle 
!=  不等于 a != b  返回值为True 
> 大于号 a > b 返回值为False 
< 小于号 a <b返回值为True 
>= 大于等于 a >= b  返回值为False 
<= 小于等于 a <= b 返回值为True

a = 5
b = 5
i = (a <= b)
print(i)
'''
#身份运算符
'''
运算符 描述 示例代码 
is is表示是否为引用同一个对象(同一个id)== 表示两边的值是否一样 a is b返回值为Fasle 
is not is表示是否不为引用同一个对象

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(id(a))
print(id(b))
print(a is b)

'''
#逻辑运算符
'''

运算符 描述 
and 同真则真：and两边同时为真结果就为真 
or 一真则真，or两边有一个为真的结果为真 
not 不真则假，不假则真 

'''
print(2<4 and 3>5)
print(True and False)

print(2<4 or 3>5)
print(True or False)

print(not 2<4)
print(not False)





































