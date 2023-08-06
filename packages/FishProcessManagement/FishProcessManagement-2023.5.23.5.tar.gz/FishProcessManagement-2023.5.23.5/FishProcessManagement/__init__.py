import os
import subprocess


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


def 显示进程池信息(进程池):
    print("当前进程池状态:")
    print("进程名\t\t进程ID\t\t已停止")
    for 进程名, (进程, pid, 已停止) in 进程池.items():
        print(f"{进程名}\t\t{pid}\t\t{已停止}")
    print()


def 进程管理器(进程列表):
    print("""
            Fishconsole 进程管理器 Versition(20230523)

                                            By 鱼鱼
    """)
    进程池 = {}

    while True:
        命令 = input("请输入命令：")
        命令列表 = 命令.split(" ")
        if 命令列表[0] == "关闭":
            进程名 = 命令列表[1]
            if 进程名 in 进程池:
                进程, pid, 已停止 = 进程池[进程名]
                if not 已停止:
                    停止子进程(进程)
                    进程池[进程名] = (进程, pid, True)
                    print("进程已关闭")
                else:
                    print("进程已经处于关闭状态")
                显示进程池信息(进程池)
            else:
                print("找不到对应的进程名字")
        elif 命令列表[0] == "启动":
            进程名 = 命令列表[1]
            if 进程名 in 进程列表:
                命令 = 进程列表[进程名]
                进程, pid = 启动子进程(命令)
                进程池[进程名] = (进程, pid, False)
                print("进程已启动")
                显示进程池信息(进程池)
            else:
                print("找不到对应的进程名字")
        else:
            print("无效的命令")
进程列表 = {
    '第一个进程': ['python', 'child.py'],
    # 其他进程信息
    }
进程管理器(进程列表)
