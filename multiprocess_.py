from multiprocessing import Process
import os


def run_proc(name):
    print('Run parent process %s(%s)' % (name, os.getppid()))
    print('Run child process %s(%s)' % (name, os.getpid()))


def run_proc0(name):
    print('Run parent process %s(%s)' % (name, os.getppid()))
    print('Run child process %s(%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process is %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))

    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    pp = Process(target=run_proc0, args=('test0', ))
    print('Child process will start.')
    pp.start()
    pp.join()
    print('Child process end.')
