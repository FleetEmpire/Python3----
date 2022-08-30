strs = input("请输入一组数据") #获取用户输入数据
lists = strs.split(" ")
new_lists = []#创建一个空列表
for i in lists:#循环转化列表
    try:
        element = int(i)
    except Exception as e:
        print(e)
    else:#将能转化的元素放在列表中
        new_lists.append(element)

print(new_lists)



'''
文件读取
file = open(r"C:\Users\Administrator\Desktop\demo.txt","r")
data = file.read()
file.close()
file = open(r"C:\Users\Administrator\Desktop\ABC\demo_abc.txt","w")
data = file.write(data)
file.close()
'''
#参考答案

file = None
data = None
file1 = None
try: 
    file = open(r"C:\Users\Administrator\Desktop\demo.txt","r")
    data = file.read()
except Exception as e:
    print(e)

finally:
    if file:
        file.close()
    
try:
    file1 = open(r"C:\Users\Administrator\Desktop\demo1.txt","w")
    data1 = file1.write(data)
except Exception as e:
    print(e)
finally:
    if file1:
        file1.close()    






















