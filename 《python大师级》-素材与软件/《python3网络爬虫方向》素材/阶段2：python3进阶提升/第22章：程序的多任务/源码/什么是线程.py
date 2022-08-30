import  time
import threading
def listening():
    for i in range(5):
        print("我在听歌")
        time.sleep(1)
def run():
    for i in range(5):
        print("我在跑步")
        time.sleep(1)
def main():
    t1 = threading.Thread(target=listening)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
if __name__ == "__main__":
    main()
