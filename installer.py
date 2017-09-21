import sys
from os import path
from constants import *


def get_full_file_name(file_name):
    return path.normcase(path.join(path.dirname(sys.argv[0]), file_name))


def prompt_user():
    dct = {'search_dir': str(input('Please specify where we can search for torrents:')),
           'extract_dir': str(input('Please specify where we can put the extracted torrents:'))}
    return dct


def create_settings_file(user_input):
    with open(get_full_file_name(SETTINGS_FILE_NAME), 'w') as f:
        for key, value in user_input.items():
            f.write(key + ';' + value + '\n')
        # not in the for loop since its not dependent on user input
        f.write('log_file_name' + ';' + get_full_file_name('log.txt') + '\n')
        f.write('error_log_file_name' + ';' + get_full_file_name('errors.txt') + '\n')


def create_log_file():
    open(get_full_file_name(LOG_FILE_NAME), 'w')


def create_error_log_file():
    open(get_full_file_name(ERROR_LOG_FILE_NAME), 'w')


def read_settings_file():
    dct = {}
    with open(get_full_file_name(SETTINGS_FILE_NAME), 'r') as f:
        lines = f.readlines()
        for line in lines:
            values = line.split(';')
            dct[values[0]] = values[1].strip()
    return dct


def file_exists(file_name):
    return path.isfile(get_full_file_name(file_name))


def run_installation():
    if (input('Installation is starting this will wipe all settings, do you want to continue? type (yes/no):')) \
            in ['yes', 'y', 'Yes', 'Y']:
        create_log_file()
        create_error_log_file()
        create_settings_file(prompt_user())
    else:
        print('Installation aborted!')
