from shelve import *


class ShelveHandler():

    def __init__(self, shelve_location):
         self.__shelve = open(shelve_location, flag='c', writeback=True)
      
    def get_completed(self):
        try:
            return self.__shelve['completed']
        except KeyError:
            return []

    def get_excluded(self):
        try:
            return self.__shelve['excluded']
        except KeyError:
            return []

    def get_setting(self, key):
        try:
            temp = self.__shelve['settings']
            self.sync()
            return temp[key]
        except KeyError:
            return None

    def set_completed(self, completed):
        try:
            temp = self.__shelve['completed']
            temp.extend(completed)
        except KeyError:
            temp = completed
        finally:
            self.__shelve['completed'] = temp
            self.sync()

    def set_excluded(self, excluded):
        try:
            temp = self.__shelve['excluded']
            temp.extend(excluded)
        except KeyError:
            temp = excluded
        finally:
            self.__shelve['excluded'] = temp
            self.sync()

    def set_setting(self, key, setting):
        try:
            temp = self.__shelve['settings']
            temp[key] = setting
        except KeyError:
            temp = {key: setting}
        finally:
            self.__shelve['settings'] = temp
            self.sync()

    def close(self):
        self.__shelve.close()

    def sync(self):
        self.__shelve.sync()