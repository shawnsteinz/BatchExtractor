from model import Files
from view import *
from tkinter import *


class Controller:
    def __init__(self):
        self.files_to_skip = []  # from global
        self.root = Tk()
        self.view = View(self.root)
        self.view.sidePanel.discover.bind(self.discover)
        self.view.sidePanel.extract.bind(self.extract)
        self.files = Files(extract_dir='', search_dir='')
        '''add the view as class vars'''

    def discover(self):
        self.files.discovery(self.read_completed_extrations)
        '''set the view to the new files'''

    def extract(self):
        for file in self.files.files:
            if file.extract() is True:
                self.write_completed_extraction(file.file_location)
            '''update progress bar and file in the mian screen'''

    def read_completed_extrations(self):
        with open('', 'r') as f:
            completed_extractions = f.readlines()
            return completed_extractions

    def write_completed_extraction(self, completed_extraction_name):
        with open('', 'a') as f:
            f.write(completed_extraction_name)

    def run(self):
        self.root.deiconify()
        self.root.mainloop()
