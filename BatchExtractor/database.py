import shelve


class ShelveHandler():

    def __init__(self):
        self.shelve = shelve.open('E:\\Test\\BatchExtractorShelve', writeback=True)
      
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

    def set_excluded(self, excluded):
        try:
            temp = self.shelve['excluded']
            temp.extend(excluded)
        except KeyError:
            temp = excluded
        finally:
            self.shelve['excluded'] = temp

    def set_setting(self, key, setting):
        try:
            temp = self.shelve['settings']
            temp[key] = setting
        except KeyError:
            temp = {key: setting}
        finally:
            self.shelve['settings'] = temp

    def close(self):
        self.shelve.sync()
        self.shelve.close()
