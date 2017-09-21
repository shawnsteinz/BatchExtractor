from os import stat, path, walk, sep
from constants import *


class ArchiveFinder:
    def __init__(self, search_dir, allowed_file_ext=('.rar', '.zip', '.7z')):
        self.search_dir = search_dir
        self.allowed_file_ext = allowed_file_ext

    def search(self, archives_to_skip):
        archives = []
        for directory_path, directory_name, files in walk(self.search_dir):
            for file_name in files:
                full_file_name = path.join(directory_path, file_name)
                condition_one = file_name.lower().endswith(tuple(self.allowed_file_ext))
                condition_two = full_file_name not in archives_to_skip
                if condition_one and condition_two:
                    archives.append(Archive(full_file_name))
        return archives


class Archive:
    def __init__(self, file_name):
        self.file_name = file_name
        self.display_name = file_name.replace(sep, '/')
        self.status = READY_FOR_EXTRACTION
