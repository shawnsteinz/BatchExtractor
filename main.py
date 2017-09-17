from controller import *

'''reading settings from file etc can happen here'''
'''checking if settings file exsit'''
'''run install instructions in cmd if not'''
global path_to_file
path_to_file = ''


if __name__ == '__main__':
    controller = Controller()
    # controller.run()
    controller.discovery()
