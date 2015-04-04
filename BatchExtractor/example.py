__author__ = 'Misja'

from BatchExtractor.database import ShelveHandler
from BatchExtractor.utility import *
from BatchExtractor.command import *

sh = ShelveHandler()
files = filter_list(sh.get_completed(), sh.get_excluded(), search(sh.get_setting('src')))
commands = []

for file in files:
    commands.append(Command(file, sh.get_setting('des')))

for command in commands:
    print(command.to_string())

handler = CommandHandler(commands)
handler.execute()

sh.set_completed(handler.completed)
sh.close()

