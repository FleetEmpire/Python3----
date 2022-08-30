#序列列表的概述
list1 = ["小明","tony","老豪",12,5.6,True,["小明","tony","老豪",12,5.6,True]]
#print(list1)

#增加列表项
'''
1、使用append（）函数增加列表项,默认添加到最后一位
2、使用extend() 函数增加多个列表项
3、使用insert()  函数增加指定列表项
4、使用+进行合并操作
'''
animal = ["老虎","狮子","大象","老鹰"]
#animal.append("小鸡")
#animal.extend("abcde")
#animal.insert(2,"小鸡")
#animals = animal1+animal
#print(animals)

#查找列表项
'''
1、使用index（）查找列表项
2、成员运算符查找：in
3、通过for循环挨个对比，每次取一个元素
'''
#animal = ["老虎","狮子","大象","老鹰","小鸡"]
#i = animal.index("小鸡")
#b = "小鸡" in animal

for i in animal:
    if "小鸡" == i:
        print("存在")
        break
    
#修改列表项
'''
1、通过对指定下标重新赋值进行修改
'''

animal = ["老虎","狮子","大象","老鹰","小鸡"]
#print(animal[3] )
#animal[2] = "猴子"
#print(animal)


#删除列表和列表项
'''
1、使用clear（）将列表清空
2、使用pop() 删除指定下标列表项
3、使用remove()  删除指定列表项
4、del 删除指定索引范围的列表

'''
animal = ["老虎","狮子","大象","老鹰","小鸡"]
#animal.clear()
#animal.pop(4)
#animal.remove("老鹰")
del animal
print(animal)

































































































