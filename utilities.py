from constants import SETTINGS_FILE_NAME
from subprocess import check_output, CalledProcessError
from os import path
from sys import argv

'''Utilities'''


def extract(archive_name, extract_dir):
    try:
        output = check_output(['7z', 'e', archive_name, '-y', '-o' + extract_dir])
    except CalledProcessError as e:
        return {'status': False, 'msg': e.output}
    else:
        return {'status': True, 'msg': output}


def write(file_name, value):
    with open(file_name, 'a') as f:
        f.write(value + '\n')


def read(file_name):
    with open(file_name, 'r') as f:
        return [l.strip() for l in f.readlines()]


def read_settings_file():
    dct = {}
    with open(path.join(path.dirname(argv[0]), SETTINGS_FILE_NAME), 'r') as f:
        lines = f.readlines()
        for line in lines:
            values = line.split(';')
            dct[values[0]] = values[1].strip()
    return dct


def file_exists(install_dir, file_name):
    return path.isfile(path.join(install_dir, file_name))
