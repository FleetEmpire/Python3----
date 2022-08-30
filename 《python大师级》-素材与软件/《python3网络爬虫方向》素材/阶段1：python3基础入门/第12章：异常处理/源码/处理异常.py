#处理异常
'''
try:
可能会报错或出现异常的代码

except Exception as e:
捕获try代码中的异常，Exception就是所捕到的异常
而e可以当成Exception的小名

else:
没有异常的时候会执行

finally:
不管有没有异常都要执行

'''

lists = [12,44,6678,3,0,34,"b",99]
for i in lists:
    #print(i)
    try:
        a = 3/i
        print(a)
  except Exception as e:
        print(e)
     else:
        print("我什么时候执行呢？")


        
