__author__ = 'Misja'

from pickle import *

database = {'completed': [], 'excluded': [], 'settings': {'origin': 'E:\Test\SRC', 'destination': 'E:\Test\DES'}}
open('E:\Test\database.pkl', 'a')
dump(database,  open('E:\Test\database.pkl', 'wb'))