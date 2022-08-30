list1 = [2,335,66,7,88,94,74,0,12]
list2 = ["and","Tfb","Jack","a","HeroLong","df","long"]

#1、sort（ reverse = False ）/sort()升序排序
'''
#list1.sort()
#list2.sort()
list1.sort(reverse = False)
list2.sort(reverse = False)
print(list1)
print(list2)
'''


#2、使用sort(reverse = True)降序排序
'''
list1.sort(reverse = True)
list2.sort(reverse = True)
print(list1)
print(list2)
'''

#3、反向排序reverse() 函数进行排序
'''
list1.reverse()
list2.reverse()
print(list1)
print(list2)
'''

#4、使用sorted（ 需要排序的序列）返回新的升序列表
'''
newlist1 = sorted(list1)
newlist2 = sorted(list2)
print(newlist1)
print(newlist2)
print(list1)
print(list2)
'''

#5、使用sort(key = len) 按照字符串长度从短到长排序
'''
list2.sort(key = len)
print(list2)
'''


#6、使用sort(key = str.lower) 大写转小写在排序
list2.sort(key = str.lower)
print(list2)

















































































