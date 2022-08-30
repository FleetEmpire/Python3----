for i in range(1,10):
        for j in range(1,i+1):
            print(str(j)+"x"+str(i)+"="+str(i*j)+" ",end = "")
        print("\n")
"""

"""

#嵌套循环
for i in range(3):
        for j in range(4):
                print("*",end = "")
        print("\n")

#嵌套可变循环
row = int(input("请输入有多少行"))
column = int(input("请输入有多少列")) 
for i in range(row):
        for j in range(column):
                print("*",end = "")
        print("\n")

#乘法表
for i in range(6):
        for j in range(0,i+1):
                print("*",end = "")
        print("\n")




















