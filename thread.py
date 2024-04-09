import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName(), " ")
        time.sleep(5)
        print("sub thread end ", threading.currentThread().getName(), " ")


print("main thread start")
# 1. 일반적인 스레드와 데몬 
# for i in range(5):
#     name = "thread {}".format(i)
#     t = Worker(name)                # sub thread 생성
#     # t.daemon = True               #데몬 
#     t.start()                       # sub thread의 run 메서드를 호출

# 2. subThread가 끝날때까지 기다리기  
# t1 = Worker("1")        # sub thread 생성
# t1.start()              # sub thread의 run 메서드를 호출

# t2 = Worker("2")        # sub thread 생성
# t2.start()              # sub thread의 run 메서드를 호출

# t1.join() # 메인 스레드가 종료 되지 않고 기다린다. 
# t2.join()

threads = []
for i in range(3):
    thread = Worker(i)
    thread.start()              # sub thread의 run 메서드를 호출
    threads.append(thread)


for thread in threads:
    thread.join()

print("main thread post job")
print("main thread end")