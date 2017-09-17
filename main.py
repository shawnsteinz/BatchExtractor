from controller import *
from installer import *

''' Settings and completed file will always next to the installer script
'''
def run(settings):
    controller = Controller(extract_dir=settings['extract_dir'],
                            search_dir=settings['search_dir'],
                            location_7zip=settings['location_7zip'],
                            location_completed_extractions=settings['location_completed_extractions'])
    controller.run()


if __name__ == '__main__':
    if(file_exists('settings.txt')) and file_exists('completed.txt'):
        run(read_settings_file())

    else :
        run_installation()
        run(read_settings_file())

