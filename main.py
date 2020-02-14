import os

from task_store import TaskList


tl = TaskList()


def list_tasks():
    for k, v in tl.task_list.items():
        print("\033[1m" + k + "\033[0m" + ": " + v)


def menu():
    cmd = input("\033[1m\033[0;36m>\033[0m ")
    if cmd[0] == "a":
        tl.add_task(cmd[2:])

    elif cmd[0] == "r":
        tl.remove_task(cmd[2:])

    elif cmd[0] == "c":
        tl.track_done_task(cmd[2:])

    elif cmd[0] == "d":
        tl.track_doing_task(cmd[2:])

    elif cmd[0] == "z":
        tl.remove_done(cmd[2:])

    elif cmd[0] == "x":
        tl.remove_doing(cmd[2:])

    elif cmd == "e":
        os.system("clear")
        exit()


while True:
    os.system("clear")
    print("\033[0;35m====================\033[0;34mTODO LIST\033[0m\033[0;35m====================\033[0m")
    list_tasks()
    print("\n")
    menu()
