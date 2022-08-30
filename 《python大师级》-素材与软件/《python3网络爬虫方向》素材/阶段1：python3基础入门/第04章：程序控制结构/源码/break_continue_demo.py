#break 和 continue停止程序执行
'''
使用break停止程序执行，可以使用在while循环中，
也可以使用在for计数循环中。如何将以下程序更改为使用break的程序。

flag = True
a = 0
while flag:
    a += 1
    print("我喜欢python")
    if a > 9:
       flag = False
'''    

a = 0
while True:
    a += 1
    print("我喜欢python")
    if a > 9:
        break
       
#continue的使用
for i in range(100):
    if i%2 == 0:
        continue
    #print(i)
    
for i in range(100):
    if i%3 == 0 and i%5 == 0:
        print(i)


























































