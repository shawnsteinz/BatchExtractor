from os import stat, path, walk


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

    def calculate_archive_size(self):
        size = 0
        for directory_path, directory_name, files in walk(path.dirname(self.file_name)):
            for file_name in files:
                if file_name.lower().endswith(tuple([".r%.2d" % i for i in range(10000)])):
                    size += stat(path.join(directory_path, file_name)).st_size
        return size

    def size(self, suffix='B'):
        number = self.calculate_archive_size()
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(number) < 1024.0:
                return "%3.1f%s%s" % (number, unit, suffix)
            number /= 1024.0
        return "%.1f%s%s" % (number, 'Yi', suffix)