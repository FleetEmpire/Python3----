#二维列表，在这个列表中还有二级子列表
list1 = [[1,2,4],[5,6,778],[5,6788,9]]
#print(list1[1][2])

#遍历列表项
'''
newlist = [23,5667,88,'sdf',"12"]
for i in newlist:
    print(i)
'''
#遍历二维列表项
newlist = []    
for i in list1:
    for j in i:
        newlist.append(j)
print(newlist)



























































