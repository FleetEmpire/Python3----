#变量命名规范：字母、下划线、数字（不能以数字开头、
#不能使用关键字、内置函数）要见名知意！
"""
a = 90
b = a
b = 23
print(a)
print(b)
"""
a = b = c = d = 90
print(a)
print(d)
print(id(a))
print(id(d))

