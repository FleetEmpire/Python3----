#增加集合元素
'''
1、通过update（）函数添加字典元素
2、通过add()函数添加。


set1 = {"12","34","345","11"}
set1.update({"14","18"})
print(set1)

set1 = {"12","34","345","11"}
set1.add("14")
print(set1)

'''
#删除集合元素
'''
1、通过pop()函数，删除最前面的一个元素；
2、通过remove()函数指定的元素。

set1 = {"12","34","345","11"}
set1.pop()
print(set1)


set1 = {"12","34","345","11"}
set1.remove("34")
print(set1)
'''
#修改字典中的元素
'''
使用update()像集合添加任意数据类型，
当为字典类型时，添加的是键，值会省略。
'''
set1 = {"12","34","345","11"}
#set1.update([23,344])
set1.update({"a":23,"b":344})
print(set1)

#查找使用in

set1 = {"12","34","345","11"}
print("12" in set1)




























