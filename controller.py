from main import path_to_file
from model import Files
from view import *
from tkinter import *


class Controller:
    def __init__(self):
        self.root = Tk()
        self.view = View(self.root)
        self.path_to_completed_extractions = r'C:\Users\Misja\Documents\filestoskip.txt'
        self.files = Files(extract_dir=r'C:\Users\Misja\Downloads\Try', search_dir=r'C:\Users\Misja\Downloads\Torrents')
        '''add the view as class vars'''

    def discovery(self):
        self.files.discovery(self.read_completed_extractions())
        '''set the view to the new files'''

    def extract(self):
        for file in self.files.files:
            if file.extract() is True:
                self.write_completed_extraction(file.file_location)
                '''update progress bar and file in the mian screen'''

    def run(self):
        self.root.deiconify()
        self.root.mainloop()

    def read_completed_extractions(self):
        with open(self.path_to_completed_extractions, 'r') as f:
            files_to_skip = f.readlines()
            return files_to_skip

    def write_completed_extraction(self, file_location):
        with open(self.path_to_completed_extractions, 'a') as f:
            f.write(file_location)