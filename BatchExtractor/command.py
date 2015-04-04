__author__ = 'Misja'


from subprocess import call


class CommandHandler():

    def __init__(self, commands):
        self.commands = commands
        self.completed = []

    def execute(self):
        for command in self.commands:
            print(command.to_string())
            return_value = call(command.to_string(), shell=True)

            if return_value == 0:
                self.completed.append(command.origin)

        return self.completed


class Command():

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def to_string(self):
        return '7z x %s -o' % self.origin + self.destination