import shelve


class ShelveHandler():

    def __init__(self, shelve_location):
         self.shelve = shelve.open(shelve_location, flag='c')
      
    def get_completed(self):
        try:
            return self.shelve['completed']
        except KeyError:
            return []

    def get_excluded(self):
        try:
            return self.shelve['excluded']
        except KeyError:
            return []

    def get_setting(self, key):
        try:
            temp = self.shelve['settings']
            self.shelve.sync()
            return temp[key]
        except KeyError:
            return None

    def set_completed(self, completed):
        try:
            temp = self.shelve['completed']
            temp.extend(completed)
        except KeyError:
            temp = completed
        finally:
            self.shelve['completed'] = temp
            self.shelve.sync()

    def set_excluded(self, excluded):
        try:
            temp = self.shelve['excluded']
            temp.extend(excluded)
        except KeyError:
            temp = excluded
        finally:
            self.shelve['excluded'] = temp
            self.shelve.sync()

    def set_setting(self, key, setting):
        try:
            temp = self.shelve['settings']
            temp[key] = setting
        except KeyError:
            temp = {key: setting}
        finally:
            self.shelve['settings'] = temp
            self.shelve.sync()

    def close(self):
        self.shelve.close()
