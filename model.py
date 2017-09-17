from subprocess import call
from os import stat, path, walk


'''Builds a list of file objects'''
class Files():
    def __init__(self, search_dir, extract_dir, allowed_file_ext=('.rar', '.zip', '.7z')):
        self.files = []
        self.search_dir = search_dir
        self.extract_dir = extract_dir
        self.allowed_file_ext = allowed_file_ext

    '''Searches a folder for files and fills the file list with file classes. 
    Optional add an additional filter to skip files'''
    def discovery(self, files_to_skip):
        for directory_path, directory_name, files in walk(self.search_dir):
            for file_name in files:
                if file_name.lower().endswith(tuple(self.allowed_file_ext)) \
                        and file_name.lower() not in files_to_skip:
                    self.files.append(File(path.join(directory_path, file_name), self.extract_dir))

'''File object that can extract himself'''
class File():
    def __init__(self, file_location, extract_destination):
        self.file_location = file_location
        self.extract_destination = extract_destination
        self.size = self.calculate_size()

    '''extracts the file by calling the command line 7zip program return True of False'''
    def extract(self):
        prm = ('7z', 'x', '-o')
        return call('%s %s %s %s%s' % (prm[0], prm[1] , self.file_location, prm[2], self.extract_destination), shell=True)

    def calculate_size(self):
        size = 0
        for directory_path, directory_name, files in walk(path.dirname(self.file_location)):
            for file_name in files:
                if file_name.lower().endswith(tuple([".r%.2d" % i for i in range(10000)])):
                    size += stat(path.join(directory_path, file_name)).st_size
        return size

    def formatted_size(self, suffix='B'):
        number = self.size
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(number) < 1024.0:
                return "%3.1f%s%s" % (number, unit, suffix)
            number /= 1024.0
        return "%.1f%s%s" % (number, 'Yi', suffix)