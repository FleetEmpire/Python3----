#如何筛选出一个给定列表的偶数
def oushu_list(listone):
    new_list = []
    for i in listone:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

#比较大小
def max_number(a,b):
    if a > b:
        return a
    else:
        return b

#冒泡排序算法
def maopao(list1):
    for j in range(0,len(list1)-1):
        for i in range(0,len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
    return list1
