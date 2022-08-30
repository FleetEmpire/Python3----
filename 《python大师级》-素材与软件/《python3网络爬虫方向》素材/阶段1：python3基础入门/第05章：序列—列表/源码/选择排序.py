#选择排序
'''
比武招亲的方式,每轮选出一个较大或者较小的数字

a = 2
b = 3
a,b = b,a
print(a)
print(b)
实现变量互换
'''
num = [34,65,28,7,15,3,55,566,0]

for j in range(0,len(num)-1):
    for i in range(1+j,len(num)):
        if num[j] < num[i]:
            num[j],num[i] = num[i],num[j]
print(num)


