import subprocess


def extract(archive_name, extract_dir):
    try:
        output = subprocess.check_output(['7z', 'e', archive_name, '-y', '-o' + extract_dir])
    except subprocess.CalledProcessError as e:
        return {'status': False, 'msg': e.output}
    else:
        return {'status': True, 'msg': output}


def write(file_name, value):
    with open(file_name, 'a') as f:
        f.write(value + '\n')


def read(file_name):
    with open(file_name, 'r') as f:
        return [l.strip() for l in f.readlines()]
