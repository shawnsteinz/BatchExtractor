__author__ = 'Misja'

from os import path, listdir


allowed_file_extensions = ('.rar', '.zip', '.7z')


def search(search_location):

    files = []
    all_files = listdir(search_location)

    for file in all_files:
        if file[-4:] in allowed_file_extensions:
            files.append(search_location + path.sep + file)
        elif path.isdir(search_location + path.sep + file):
            new_files = search(search_location + path.sep + file)
            if new_files:
                for new_file in new_files:
                    files.append(new_file)

    return files


def filter_list(completed, excluded, files):

        filtered_list = []

        for file in files:
            if file not in completed or file not in excluded:
                filtered_list.append(file)

        return filtered_list