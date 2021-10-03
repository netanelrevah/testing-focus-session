from datetime import datetime


def extract_year(value):
    if isinstance(value, int):
        return value
    if isinstance(value, datetime):
        return value.year
    raise NotImplementedError


class Worker(object):
    def __init__(self, task, name=None):
        self.task = task
        self.name = name

    def work_hard(self):
        self.task.run()

    def rest(self):
        pass

    def set_rest_time(self, rest_time):
        pass

    def fire(self):
        pass


class FastWorker(Worker):
    pass


class Connection(object):
    def __init__(self, port):
        self.port = port

    def connect(self):
        pass

    def disconnect(self):
        pass
