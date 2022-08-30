#集合运算
#交运算
'''
#1、交集使用intersection()函数/&符号表示；
set1 = {"12","34","345","11"}
set2 = {"122","34","5","11"}
#new_set = set2.intersection(set1)
new_set = set1 & set2
print(new_set)
'''
#并运算
'''
#1、并集使用 union()函数/|符号表示
set1 = {"12","34","345","11"}
set2 = {"122","34","5","11"}
#new_set = set2.union(set1)
new_set = set1 | set2
print(new_set)
'''
#差运算
'''
1、差集使用 difference()函数表示；

set1 = {"12","34","345","11"}
set2 = {"122","34","5","11"}
new_set = set1.difference(set2)
print(new_set)
'''

#对称差集
#1、对称差集使用 symmetric_difference ()函数表示；
set1 = {"12","34","345","11"}
set2 = {"122","34","5","11"}
new_set = set1.symmetric_difference(set2)
print(new_set)



























































