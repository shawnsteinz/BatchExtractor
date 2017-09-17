from controller import *

'''reading settings from file etc can happen here'''
'''checking if settings file exsit'''
'''run install instructions in cmd if not'''

if __name__ == '__main__':
    controller = Controller(extract_dir=r'C:\Users\Misja\Downloads\Torrents',
                            search_dir=r'C:\Users\Misja\Downloads\Extracted Torrents',
                            completed_path=r'C:\Users\Misja\Downloads\completed_extractions.txt')
    controller.run()

