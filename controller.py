from model import Files
from view import *
from tkinter import *


class Controller:
    def __init__(self):
        self.files_to_skip = []  # from global
        self.root = Tk()
        self.view = View(self.root)
        self.view.sidePanel.dicovery.bind(self.dicovery)
        self.view.sidePanel.extract.bind(self.extract)
        self.files = Files(allowed_file_ext=['.rar', '.zip', '.7z'], extract_dir='', files_to_skip=self.files_to_skip,
                           search_dir='')
        '''add the view as class vars'''

    def dicovery(self):
        self.model.discovery()
        '''set the view to the new files'''

    def extract(self):
        for file in self.model.files:
            file.extract()
            '''update progress bar and file in the mian screen'''
            '''updated the files to skip list'''
        '''write the files to skip to file'''

    def run(self):
        self.root.deiconify()
        self.root.mainloop()
