from os import path, makedirs
from constants import LOG_FILE_NAME, ERROR_LOG_FILE_NAME, SETTINGS_FILE_NAME, RUN_SCRIPT_NAME
from sys import argv, executable
from winshell import shortcut, desktop


def prompt_user():
    dct = {'install_dir': str(input('Please tell us where we can install Unpacky?:')),
           'search_dir': str(input('Can you point us to you downloads folder?:')),
           'extract_dir': str(input('Last question where might we unpack the archives?:'))}
    return dct


def store_settings(settings):
    with open(path.join(settings['install_dir'], SETTINGS_FILE_NAME), 'w+') as f:
        for key, value in settings.items():
            f.write(key + ';' + value + '\n')
        # not in the for loop since its not dependent on user input
        f.write('log_file_name' + ';' + path.join(settings['install_dir'], LOG_FILE_NAME) + '\n')
        f.write('error_log_file_name' + ';' + path.join(settings['install_dir'], ERROR_LOG_FILE_NAME) + '\n')


def create_files(install_dir, file_names):
    for file_name in file_names:
        f = open(path.join(install_dir, file_name), 'w')
        f.close()


def create_single_script(install_dir, script_name):
    scripts = ['constants.py', 'controller.py', 'model.py', 'utilities.py', 'view.py', 'main.py']
    modules = [i[:-3] for i in scripts] # strip the extensions '.py'
    imports = []
    code = []

    if not path.exists(install_dir):
        makedirs(install_dir)

    '''Collecting all relevant information form the scripts'''
    for script in scripts:
        with open(path.join(path.dirname(argv[0]), script), 'r') as f:
            lines = f.readlines()
            imports.extend([l for l in lines if l not in imports 
                            and l.startswith(('import', 'from'))
                            and l.split()[1] not in modules])
            code.extend([l for l in lines if not l.startswith(('import', 'from'))])

    '''Writing all relevant information into a single file'''
    with open(path.join(install_dir, script_name), 'w') as f:
        for line in imports:
            f.write(line)
        f.write('\n\n')
        for line in code:
            f.write(line)

def create_shortcut(installpath):
    filepath = path.join(desktop(), 'Unpacky.lnk')
    with shortcut(filepath) as link:
        link.path = executable
        link.description = "Shortcut to Unpacky"
        link.arguments = path.join(installpath, RUN_SCRIPT_NAME)
        link.write()


def run_installation():
    if (input('Installation is starting this will wipe all settings, do you want to continue? type (yes/no):')) \
            in ['yes', 'y', 'Yes', 'Y']:

        settings = prompt_user()
        create_files(settings['install_dir'], [ERROR_LOG_FILE_NAME, SETTINGS_FILE_NAME, LOG_FILE_NAME])
        store_settings(settings)
        create_single_script(settings['install_dir'], RUN_SCRIPT_NAME)
        if (input('Would you like us to add a shortcut on your desktop? type (yes/no):')) in ['yes']:
            create_shortcut(settings['install_dir'])
    else:
        print('Installation aborted!')


run_installation()