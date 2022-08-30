#有参函数
'''
def max_number(a,b):
    if a > b:
        print("最大值为",a)
    else:
        print("最大值为",b)
        
max_number(12,674)
'''
#有参函数—冒泡排序
'''
list1 = [23,56,5,61,6,45,7,789,0,1000,2]

for j in range(0,len(list1)-1):
    for i in range(0,len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
'''
list1 = [23,56,5,61,6,45,7,789,0,1000,2]

def maopao(list1):
    for j in range(0,len(list1)-1):
        for i in range(0,len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
maopao(list1)       
print(list1)































