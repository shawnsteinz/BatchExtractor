__author__ = 'Misja'


from subprocess import call


class CommandHandler():

    def __init__(self, commands):
        self.commands = commands
        self.completed = []

    def execute(self):
        for command in self.commands:
            return_value = call(command.to_string(), shell=True)

            if return_value == 0:
                self.completed.append(command.origin)


class Command():

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def to_command(self):
        return '7z x -oas %s -o' % self.origin + self.destination