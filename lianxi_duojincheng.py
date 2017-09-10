from multiprocessing import Process, Pool, cpu_count
from threading import Thread, current_thread
import os, time, random


def process0(name):
    start = time.time()
    print('%s\'s pid is:%s' % (name, os.getpid()))
    time.sleep(5)
    end = time.time()
    print(name,' use ',end-start,' time!')
start = (time.time())
if __name__ == '__main__':
    print('%s\'s pid is:%s' % ('father', os.getpid()))
    print('****************多进程************************')
    P = Process(target=process0, args=('child0', ))
    P.start()
    P.join()
    print('****************进程池************************')
    Pl = Pool(cpu_count())
    for i in range(cpu_count()):
        process0(i)
 #       Pl.apply_async(process0, args=(i, ))
 #   Pl.close()
 #   Pl.join()
end = (time.time())
print(end-start)
