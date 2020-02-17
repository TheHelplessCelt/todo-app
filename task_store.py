import time
import calendar
import os
import atexit
import json


def get_time():
    # TODO actually use this
    return calendar.timegm(time.gmtime())


class TaskList:
    def __init__(self):
        self.task_list = {}
        self.read_tasks()
        atexit.register(self.save_tasks)

    def add_task(self, row):
        """adds the description of a task to task_list dict

        Arguments:
            row {string} -- the description of a task
        """
        if len(self.task_list) == 0:
            self.task_list["0"] = row
        else:
            keys = self.task_list.keys()
            keys = [int(x) for x in keys]
            self.task_list[str(max(keys) + 1)] = row

    def remove_task(self, id):
        """removes a task at the specified index

        Arguments:
            id {int} -- the index to remove
        """
        try:
            del self.task_list[id]
        except KeyError:
            print("not a valid id")

    def save_tasks(self):
        """writes the task list to a json file upon close
        """

        with open("task_list.json", "w+") as js_file:
            json.dump(self.task_list, js_file)

    def read_tasks(self):
        """read the task list json at launch
        """

        if os.path.exists("task_list.json"):
            with open("task_list.json", "r") as js_file:
                self.task_list = dict(json.load(js_file))

    def remove_done(self, id):
        """removes the done tag from a specified tag

        Arguments:
            id {int} -- the task to remove the tag from
        """

        try:
            row = self.task_list[id]
        except KeyError:
            print("not a valid id")

        self.task_list[id] = row.replace("\033[0;32m ✓\033[0m", "")

    def remove_blocked(self, id):
        """removes the blocked tag from a specified tag

        Arguments:
            id {int} -- the task to remove the tag from
        """

        try:
            row = self.task_list[id]
        except KeyError:
            print("not a valid id")

        self.task_list[id] = row.replace("\033[0;31m ✗\033[0m", "")

    def remove_doing(self, id):
        """removes the doing tag from a specified tag

        Arguments:
            id {int} -- the task to remove the tag from
        """

        try:
            row = self.task_list[id]
        except KeyError:
            print("not a valid id")
        self.task_list[id] = row.replace("\033[1;33m ●\033[0m", "")

    def track_done_task(self, id):
        """adds the unicode character for a completed task, removes the blocked or doing tags

        Arguments:
            id {int} -- the task to add the tag to
        """
        try:
            if "●" in self.task_list[id]:
                self.task_list[id] = self.task_list[id].replace("\033[1;33m ●\033[0m", "\033[0;32m ✓\033[0m")
            elif "✗" in self.task_list[id]:
                self.task_list[id] = self.task_list[id].replace("\033[0;31m ✗\033[0m", "\033[0;32m ✓\033[0m")
            else:
                self.task_list[id] += "\033[0;32m ✓\033[0m"
        except KeyError:
            print("not a valid id")

    def track_doing_task(self, id):
        """adds the unicode character for an in progress task, removes the blocked or done tags

        Arguments:
            id {int} -- the task to add the tag to
        """
        try:
            if "✓" in self.task_list[id]:
                self.task_list[id] = self.task_list[id].replace("\033[0;32m ✓\033[0m", "\033[1;33m ●\033[0m")
            elif "✗" in self.task_list[id]:
                self.task_list[id] = self.task_list[id].replace("\033[0;31m ✗\033[0m", "\033[1;33m ●\033[0m")
            else:
                self.task_list[id] += "\033[1;33m ●\033[0m"
        except KeyError:
            print("not a valid id")

    def track_blocked_task(self, id):
        """adds the unicode character for a blocked task, removes the doing or done tags

        Arguments:
            id {int} -- the task to add the tag to
        """
        try:
            if "✓" in self.task_list[id]:
                self.task_list[id] = self.task_list[id].replace("\033[0;32m ✓\033[0m", "\033[0;31m ✗\033[0m")
            elif "●" in self.task_list[id]:
                self.task_list[id] = self.task_list[id].replace("\033[1;33m ●\033[0m", "\033[0;31m ✗\033[0m")
            else:
                self.task_list[id] += "\033[0;31m ✗\033[0m"
        except KeyError:
            print("not a valid id")
