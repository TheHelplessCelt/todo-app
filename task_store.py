import time
import calendar
import os
import atexit
import json


def get_time():
    return calendar.timegm(time.gmtime())


class TaskList:
    def __init__(self):
        self.task_list = {}
        self.read_tasks()
        atexit.register(self.save_tasks)

    def add_task(self, row):
        if len(self.task_list) == 0:
            self.task_list["0"] = row
        else:
            keys = self.task_list.keys()
            keys = [int(x) for x in keys]
            self.task_list[str(max(keys) + 1)] = row

    def remove_task(self, id):
        del self.task_list[id]

    def save_tasks(self):
        with open("task_list.json", "w+") as js_file:
            json.dump(self.task_list, js_file)

    def read_tasks(self):
        if os.path.exists("task_list.json"):
            with open("task_list.json", "r") as js_file:
                self.task_list = dict(json.load(js_file))

    def remove_done(self, id):
        row = self.task_list[id]
        self.task_list[id] = row.replace("\033[0;32m ✓\033[0m", "")

    def remove_doing(self, id):
        row = self.task_list[id]
        self.task_list[id] = row.replace("\033[1;33m ●\033[0m", "")

    def track_done_task(self, id):
        if "●" in self.task_list[id]:
            self.task_list[id] = self.task_list[id].replace("\033[1;33m ●\033[0m", "\033[0;32m ✓\033[0m")
        else:
            self.task_list[id] += "\033[0;32m ✓\033[0m"

    def track_doing_task(self, id):
        if "✓" in self.task_list[id]:
            self.task_list[id] = self.task_list[id].replace("\033[0;32m ✓\033[0m", "\033[1;33m ●\033[0m")
        else:
            self.task_list[id] += "\033[1;33m ●\033[0m"
