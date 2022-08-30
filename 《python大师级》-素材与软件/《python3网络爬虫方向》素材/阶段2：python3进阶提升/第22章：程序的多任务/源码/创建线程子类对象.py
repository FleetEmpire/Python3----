import threading

class mythread(threading.Thread):
    def run(self):
        for i in range(10):
            print("我喜欢python")
        self.abc()
    def abc(self):
        for i in range(10):
            print("我喜欢c++")



if __name__ == "__main__":
    m = mythread()
    m.start()
