
from os import stat, path, walk
from operator import attrgetter
from datetime import datetime


class File():

    def __init__(self, file_location):
        statistics = stat(file_location)
        self.location = file_location
        self.size = statistics.st_size
        self.archive_size = self.__size()
        self.creation_time = statistics.st_ctime

    def __size(self):
        size = self.size
        for directory_path, directory_name, files in walk(path.dirname(self.location)):
            for file_name in files:
                if file_name.lower().endswith(tuple([".r%.2d" % i for i in range(1000)])):
                    size = size + stat(path.join(directory_path, file_name)).st_size

        return size

    def get_location(self):
        return self.location

    def get_creation_datetime(self):
        d = datetime.fromtimestamp(self.creation_time)
        return d.ctime()

    def get_size(self, suffix='B'):
        number = self.archive_size
        for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
            if abs(number) < 1024.0:
                return "%3.1f%s%s" % (number, unit, suffix)
            number /= 1024.0

        return "%.1f%s%s" % (number, 'Yi', suffix)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class FileList():

    def __init__(self, top_directory, allowed_file_extensions):
        self.files = []
        self.allowed_file_extensions = allowed_file_extensions
        self.__fill(top_directory)

    def __fill(self, top_directory):
        for directory_path, directory_name, files in walk(top_directory):
            for file_name in files:
                if file_name.lower().endswith(tuple(self.allowed_file_extensions)):
                    self.files.append(File(path.join(directory_path, file_name)))

    def remove_files_by_tasks(self, excluded_tasks=[], completed_tasks=[]):
        task_list = []

        if excluded_tasks or completed_tasks:
            if excluded_tasks:
                task_list.extend(excluded_tasks)
            if completed_tasks:
                task_list.extend(completed_tasks)

        for task in task_list:
            self.__remove_file(task.file)

    def __remove_file(self, file):
        for tmpfile in self.files:
            if tmpfile == file:
                self.files.remove(tmpfile)
            break

    def sort(self, attribute, descending=True):
        for method in [x for x in dir(self) if callable(getattr(self, x)) and 'sort_by_' in x]:
            if attribute in method:
                getattr(self, method)(descending)
                break

    def __sort_by_date(self, descending):
        self.files = sorted(self.files, key=attrgetter('creation_time'), reverse=descending)

    def __sort_by_size(self, descending):
        self.files = sorted(self.files, key=attrgetter('archive_size'), reverse=descending)

    def get_files(self):
        return self.files


