import os

from task_store import TaskList


tl = TaskList()


def list_tasks():
    for k, v in tl.task_list.items():
        print(k + ": " + v)


def menu():
    cmd = input("> ")

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
    list_tasks()
    print("\n")
    menu()
