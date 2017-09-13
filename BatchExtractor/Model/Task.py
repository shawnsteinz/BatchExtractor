from subprocess import call

class TaskHandler():

    def __init__(self, file_list, destination_directory):
        self.__tasks = self.__create_tasks(file_list, destination_directory)
        self.successful_tasks = []
        self.failed_tasks =[]

    def __create_tasks(self, file_list, destination_directory):
        tasks = []
        for file in file_list:
            tasks.append(Task(file, destination_directory))

        return tasks

    def execute_tasks(self):
        for task in self.__tasks:
            return_value = call(task.to_cmd(), shell=True)

            if return_value == 0:
                self.successful_tasks.append(task)
            elif return_value == 1:
                self.failed_tasks.append(task)

    def get_tasks(self):
        return self.__tasks

class Task():

    def __init__(self, file, destination_directory, parameters=('7z', 'x', '-o')):
        self.file = file
        self.destination_directory = destination_directory
        self.parameters = parameters

    def to_cmd(self):
        prm = self.parameters
        return '%s %s %s %s%s' % (prm[0], prm[1] , self.file.location, prm[2], self.destination_directory)
