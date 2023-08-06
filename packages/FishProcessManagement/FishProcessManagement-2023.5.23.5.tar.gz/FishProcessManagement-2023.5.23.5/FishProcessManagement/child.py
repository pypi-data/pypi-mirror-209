import multiprocessing
import time

def worker(num):
    """子进程"""
    print('子进程 %d 开始执行' % num)
    sub_process = multiprocessing.Process(target=sub_worker, args=(num,))
    sub_process.start()
    while True:
       time.sleep(1)
       print('子进程正在运行')

def sub_worker(num):
    """子子进程"""
    while True:
       time.sleep(1)
       print('子子进程 %d 开始执行' % num)
    
   

def main():
    # 主进程
    print('主进程开始执行')
    process1 = multiprocessing.Process(target=worker, args=(1,))
    process1.start()
    process1.join()
    print('主进程执行完毕')

if __name__ == '__main__':
    main()