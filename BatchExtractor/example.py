__author__ = 'Misja'

from BatchExtractor.database import DatabaseHandler
from BatchExtractor.utility import *
from BatchExtractor.command import *

db = DatabaseHandler('E:\Test\database.pkl')
files = filter(db.get_completed(), db.get_excluded(), search(db.get_setting('origin')))
commands = []

for file in files:
    commands.append(Command(file, db.get_setting('destination')))

handler = CommandHandler(commands)
handler.execute()

db.set_completed(handler.completed)
db.save()




