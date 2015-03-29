from pickle import *


class DatabaseHandler():

    def __init__(self, location):
        self.location = location
        file = open(self.location, 'rb')
        self.database = load(file)
      
    def get_completed(self):
        return self.database['completed']

    def get_excluded(self):
        return self.database['excluded']

    def get_setting(self, index):
        return self.database['settings'][index]

    def set_completed(self, completed):
        self.database['completed'] + completed

    def set_excluded(self, excluded):
        self.database['excluded'] + excluded

    def set_setting(self, index, setting):
        self.database['setting'][index] = setting

    def save(self):
        dump(self.database,  open(self.location, 'wb'))
