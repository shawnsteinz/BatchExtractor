import shelve


class ShelveHandler():

    def __init__(self):
        self.shelve = None
      
    def get_completed(self):
        try:
            self.open()
            return self.shelve['completed']
            self.close()
        except KeyError:
            return []

    def get_excluded(self):
        try:
            self.open()
            return self.shelve['excluded']
            self.close()
        except KeyError:
            return []

    def get_setting(self, key):
        try:
            self.open()
            temp = self.shelve['settings']
            self.close()
            return temp[key]
        except KeyError:
            return None

    def set_completed(self, completed):
        self.open()
        try:
            temp = self.shelve['completed']
            temp.extend(completed)
        except KeyError:
            temp = completed
        finally:
            self.shelve['completed'] = temp
            self.close()

    def set_excluded(self, excluded):
        self.open()
        try:
            temp = self.shelve['excluded']
            temp.extend(excluded)
        except KeyError:
            temp = excluded
        finally:
            self.shelve['excluded'] = temp
            self.close()

    def set_setting(self, key, setting):
        self.open()
        try:
            temp = self.shelve['settings']
            temp[key] = setting
        except KeyError:
            temp = {key: setting}
        finally:
            self.shelve['settings'] = temp
            self.close()

    def close(self):
        self.shelve.sync()
        self.shelve.close()
        self.shelve = None

    def open(self):
        self.shelve = shelve.open('E:\\Test\\BatchExtractorShelve', writeback=True)
