strs = input("请输入一组有空格的数字")
lists = strs.split(" ")
if len(lists) >= 5:
    print(lists)
else:
    #创建异常对象
    e = Exception("列表长度少于5")
    #抛出异常
    raise e
