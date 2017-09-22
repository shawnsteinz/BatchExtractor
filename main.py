from controller import *
from utilities import *

'''Main'''

if __name__ == '__main__':
    settings = read_settings_file()
    if settings:
        controller = Controller(settings['extract_dir'], settings['search_dir'], settings['log_file_name'],
                                    settings['error_log_file_name'])
        controller.run()
    else:
        print('Sorry can you plz run installer.py first!')
