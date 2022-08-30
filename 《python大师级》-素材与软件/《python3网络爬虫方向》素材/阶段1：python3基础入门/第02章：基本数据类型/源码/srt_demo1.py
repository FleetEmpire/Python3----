name1 = '小明'
name2 = "小明"
name3 = """
我是小明
"""
print(name1)
print(name2)
print(name3)

#字符串的读取操作
name = "abcsdafdf,h"
print(name[:4])
print(name[2:4])
print(name[9:])
print(name[:])

#字符串的合并
first_name = "Guido"
last_name = "van Rossum"
new_name = first_name+" "+last_name
print(new_name)

#字符串的修改
new_name1 = new_name[:9]+" "+"python"
print(new_name1)

new_name2 = new_name1.replace("python","a")
print(new_name2)
#Guido van a

#字符串的删除
del(new_name2)




















