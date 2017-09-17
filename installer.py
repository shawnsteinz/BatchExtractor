import sys
import os


def file_location(file_name):
    return os.path.normcase(os.path.join(os.path.dirname(sys.argv[0]), file_name))


def prompt():
    dct = {}
    dct['location_7zip'] = str(input('Please input your path to 7zip:'))
    dct['search_dir'] = str(input('Please input your path to torrents:'))
    dct['extract_dir'] = str(input('Please input your path where you would like to extract the torrents:'))
    return dct


def create_settings_file(user_input):
    with open(file_location(file_name='settings.txt') , 'w') as f:
        for key, value in user_input.items():
            f.write(key + ';' + value + '\n')
        # not in the for loop since its not dependent on user input
        f.write('location_completed_extractions' + ';' + file_location('completed.txt'))


def create_completed_file():
    open(file_location(file_name='completed.txt'), 'w')


def read_settings_file():
    dct = {}
    with open(file_location(file_name='settings.txt'), 'r') as f:
        lines = f.readlines()
        for line in lines:
            values = line.split(';')
            dct[values[0]] = values[1].strip()
    return dct;

def file_exists(file_name):
    return os.path.isfile(file_location(file_name=file_name))


def run_installation():
    if (input('Installation is starting this will wipe all settings, do you want to continue? type (yes/no)')) \
            in ['yes', 'y', 'Yes', 'Y']:
        create_completed_file()
        create_settings_file(prompt())
    else :
        print('Installation aborted')
