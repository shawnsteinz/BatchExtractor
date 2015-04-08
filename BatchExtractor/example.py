__author__ = 'Misja'

from BatchExtractor.database import ShelveHandler
from BatchExtractor.utility import *
from BatchExtractor.task import *

sh = ShelveHandler()
files = filter_list(sh.get_completed(), sh.get_excluded(), search(sh.get_setting('src'), sh.get_setting('ext')))
commands = []

for file in files:
    commands.append(Task(file, sh.get_setting('des')))

for command in commands:
    print(command.to_string())

handler = TaskHandler(commands)
handler.execute_tasks()

sh.set_completed(handler.completed)


