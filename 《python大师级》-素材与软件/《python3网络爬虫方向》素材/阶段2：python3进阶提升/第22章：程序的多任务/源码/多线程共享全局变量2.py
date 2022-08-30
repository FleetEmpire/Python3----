import threading
import time
num = 0
a = 1000000

def text1(times):
    global num
    for i in range(times):
        num+=1
    print(num)

def text2(times):
    global num
    for i in range(times):
        num += 1
    print(num)

def main():
    t1 = threading.Thread(target=text1,args=(a,))
    t2 = threading.Thread(target=text2,args = (a,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print(num)

if __name__ == "__main__":
    main()
