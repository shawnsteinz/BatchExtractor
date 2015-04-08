__author__ = 'Misja'


from subprocess import call


class TaskHandler():

    def __init__(self, tasks):
        self.tasks = tasks
        self.completed_tasks = []
        self.execution_time = 0

    def execute_tasks(self):
        for task in self.tasks:
            return_value = call(task.to_cmd(), shell=True)

            if return_value == 0:
                self.completed_tasks.append(task.source)

        return self.completed_tasks


class Task():

    def __init__(self, source, destination, options=('7z', 'x', '-o')):
        self.source = source
        self.destination = destination
        self.options = options

    def to_cmd(self):
        x = self.options
        return x[0] + ' ' + x[1] + ' ' + self.source + ' ' + x[2] + self.destination