import time
import random
#猜数字游戏
print("------------猜数字------------")
time.sleep(1)
print("----游戏开始啦----")
for i in range(3):
    time.sleep(1)
    print(str(i+1))
num = random.randint(0,9)
print("随机数已经出现了")
for i in range(3):
    a = int(input("请输入您所猜的数字"))
    if a > num:
        print("您猜测大了")
    elif a< num:
        print("您猜测小了")
    else:
        print("恭喜您猜测对了，您真聪明")
        break
    
    
