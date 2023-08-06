import os
import subprocess
import signal


def 停止子进程(进程):
    if os.name == 'nt':
        subprocess.run(['taskkill', '/F', '/T', '/PID', str(进程.pid)], shell=True)
    else:
        def 杀死进程树(pid):
            # 查找进程及其子进程的PID列表
            子进程pid列表 = os.popen('pgrep -P {}'.format(pid)).read().splitlines()

            # 递归终止进程及其子进程
            for 子进程pid in 子进程pid列表:
                杀死进程树(子进程pid)

            # 终止给定PID的进程
            os.system('kill -9 {}'.format(pid))

        杀死进程树(进程.pid)


def 启动子进程(命令):
    if os.name == 'nt':
        shell = True
    else:
        shell = False
    进程 = subprocess.Popen(命令, shell=shell)
    return 进程, 进程.pid


def 进程管理器(进程列表):
    print("""
            Fishconsole 进程管理器 Versition(20230523)

                                            By 鱼鱼
    """)
    进程池 = []
    进程名池 = []
    for 进程 in 进程列表:
        进程名池.append(进程[0])
    while True:
        命令 = input("请输入命令：")
        命令列表 = 命令.split(" ")
        if 命令列表[0] == "关闭":
            进程名 = 命令列表[1]
            try:
                进程索引 = 进程名池.index(进程名)
                进程, pid = 进程池[进程索引]
                停止子进程(进程)
                进程名池.remove(进程名)
                进程池.remove([进程, pid])
                print("进程已关闭")
            except ValueError:
                print("找不到对应的进程名字")
        elif 命令列表[0] == "启动":
            进程名 = 命令列表[1]
            try:
                进程索引 = 进程名池.index(进程名)
                进程, pid = 启动子进程(进程列表[进程索引][1])
                进程池.append((进程, pid))
            except ValueError:
                print("找不到对应的进程名字")
        else:
            print("无效的命令")


# 进程列表 = [
#         ['第一个进程', ['python', 'child.py']],
#         # 其他进程信息
#     ]
# 进程管理器(进程列表)