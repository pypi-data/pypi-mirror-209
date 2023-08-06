>  我利用了几乎所有的业余时间设计了Fishconsole Project，虽然现在十分拉跨，但正努力前行

- 它是一个启动python项目的工具
----

# 🦈FishProcessManagement 小鱼进程管理器功能一览
##### 
- 启动 你的项目名
- 关闭 你的项目名
------------



- 主进程


import FishProcessManagement
进程列表 = [
['第一个进程', ['python', 'child.py']],
]
FishProcessManagement.进程管理器(进程列表)








- 子进程

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




-----------





# 🦈FishProcessManagement 小鱼进程管理器 2023.5.23

1. 打包成python的库
-----------


