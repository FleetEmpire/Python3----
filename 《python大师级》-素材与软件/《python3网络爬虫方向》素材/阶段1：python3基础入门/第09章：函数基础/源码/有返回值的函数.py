#有返回值得函数创建
'''
def max_num(a,b):
    if a > b:
        return a
    else:
        return b
m = max_num(34,6)
print(m)

'''
#如何筛选出一个给定列表的偶数

list1 = [21,34,23,4,23,567,8,909,0,23]

def oushu_list(listone):
    new_list = []
    for i in listone:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

list_new = oushu_list(list1)
print(list_new)

















