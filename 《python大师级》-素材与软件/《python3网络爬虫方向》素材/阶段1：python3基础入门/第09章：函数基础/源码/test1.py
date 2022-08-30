'''
四种调用方式：
1.import + 模块名
2.import + 模块名 + as + 变量名
3.from + 模块名 + import + 函数名
4.from + 模块名 + import + 星号
'''
'''
在其他文件夹下调用模块
import sys
sys.path.append(r"")
'''
#import math_module
#import math_module as m
#from math_module import oushu_list
from math_module import *
list1 = [123,4,23,5,6,7,78]
new_list = oushu_list(list1)
#new_list = maopao(list1)
print(new_list)
