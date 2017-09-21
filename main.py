from controller import *
from installer import *


def run_app(settings):
    controller = Controller(settings['extract_dir'], settings['search_dir'], settings['log_file_name'], settings['error_log_file_name'])
    controller.run()


if __name__ == '__main__':
    condition_one = file_exists(LOG_FILE_NAME)
    condition_two = file_exists(SETTINGS_FILE_NAME)
    condition_three = file_exists(ERROR_LOG_FILE_NAME)

    if condition_one or condition_two or condition_three:
        run_app(read_settings_file())
    else:
        run_installation()
        run_app(read_settings_file())

