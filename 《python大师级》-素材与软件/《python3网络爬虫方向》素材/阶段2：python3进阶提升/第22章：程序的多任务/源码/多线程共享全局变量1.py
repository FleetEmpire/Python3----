import threading
import time
num = 100

def text1():
    global num
    num+=1
    print(num)

def text2():
    global num
    print(num)

def main():
    t1 = threading.Thread(target=text1)
    t2 = threading.Thread(target=text2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print(num)

if __name__ == "__main__":
    main()
