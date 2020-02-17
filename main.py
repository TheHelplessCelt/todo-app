import os

from task_store import TaskList

# Initialize the task list
tl = TaskList()


def list_tasks():
    """displays currently open tasks
    """
    for k, v in tl.task_list.items():
        print("\033[1m" + k + "\033[0m" + ": " + v)


def menu():
    """command menu, run multiple times, messy but works
    """

    # accept user input for command
    cmd = input("\033[1m\033[0;36m>\033[0m ")

    # command parsing
    if cmd[0] == "a" and cmd[1] == " ":
        tl.add_task(cmd[2:])

    elif cmd[0] == "r" and cmd[1] == " ":
        tl.remove_task(cmd[2:])

    elif cmd[0] == "c" and cmd[1] == " ":
        tl.track_done_task(cmd[2:])

    elif cmd[0] == "d" and cmd[1] == " ":
        tl.track_doing_task(cmd[2:])

    elif cmd[0] == "b" and cmd[1] == " ":
        tl.track_blocked_task(cmd[2:])

    elif cmd[0] == "z" and cmd[1] == " ":
        tl.remove_done(cmd[2:])

    elif cmd[0] == "x" and cmd[1] == " ":
        tl.remove_doing(cmd[2:])

    elif cmd[0] == "v" and cmd[1] == " ":
        tl.remove_blocked(cmd[2:])

    elif cmd == "e":
        os.system("clear")
        exit()

    # pass used to catch unwanted input
    else:
        pass


while True:
    # clear the screen every run to avoid ncurses
    os.system("clear")
    print("\033[0;35m====================\033[0;34mTODO LIST\033[0m\033[0;35m====================\033[0m")
    list_tasks()
    print("\n")
    menu()
