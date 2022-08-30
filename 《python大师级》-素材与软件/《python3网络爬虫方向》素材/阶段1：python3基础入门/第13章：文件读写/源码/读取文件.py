# 读取文件
'''
file = open("demo.txt","r")
str_file = file.read()
print(str_file)
file.close()
'''

# 写入文件
f = open(r"demo.txt", "w")
a = f.write("星星知我心")
f.close()
