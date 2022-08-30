import threading
import time
num = 1000000
thnum = 0
#创建互斥锁
mutex=threading.Lock()
def test1(num1):
	global thnum
	#mutex.acquire()  #等待可以上锁，
	for i in range(num1):
		thnum+=1
	print(thnum)
	#mutex.release()#解锁


def test2(num1):
    global thnum
    #mutex.acquire()  # 等待可以上锁
    for i in range(num1):
        thnum += 1
    print(thnum)
    #mutex.release()  # 解锁

def main():
    t1 = threading.Thread(target=test1,args=(num,))
    t2 = threading.Thread(target=test2, args=(num,))
    t1.start()
    t2.start()
    print(thnum)

if __name__=='__main__':
    main()
