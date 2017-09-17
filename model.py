from subprocess import call
from os import path, walk

'''Builds a list of file objects'''
class Files():
    def __init__(self, search_dir, extract_dir, allowed_file_ext, files_to_skip):
        self.files = []
        self.search_dir = search_dir
        self.allowed_file_ext = allowed_file_ext
        self.extract_dir = extract_dir
        self.files_to_skip = files_to_skip

    '''Searches a folder for files and fills the file list with file classes'''
    def discovery(self):
        for directory_path, directory_name, files in walk(self.search_dir):
            for file_name in files:
                if file_name.lower().endswith(tuple(self.allowed_file_ext)) \
                        and file_name.lower() not in self.files.to_skip:
                    self.files.append(File(path.join(directory_path, file_name, self.extract_dir)))

'''File object that can extract himself'''
class File():
    def __init__(self, file_location, extract_destination):
        self.file_location = file_location
        self.extract_destination = extract_destination

    '''extracts the file by calling the command line 7zip program return True of False'''
    def extract(self):
        prm = ('7z', 'x', '-o')
        return call('%s %s %s %s%s' % (prm[0], prm[1] , self.file_location, prm[2], self.extract_destination), shell=True)


