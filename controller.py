from model import Files
from view import *
from tkinter import *


class Controller:
    def __init__(self, extract_dir, search_dir, completed_path):
        self.root = Tk()
        self.view = View(self.root)
        self.view.sidePanel.discover.bind("<Button>", self.discover)
        self.view.sidePanel.extract.bind("<Button>", self.extract)
        self.files = Files(extract_dir=extract_dir, search_dir=search_dir)
        self.completed_path = completed_path
        '''add the view as class vars'''

    def discover(self, event):
        self.files.discovery(self.read_completed_extractions)
        self.view.fill_tree(self.files)
        
    def extract(self):
        for file in self.files.files:
            if file.extract() is True:
                self.write_completed_extraction(file.file_location)
            '''update progress bar and file in the mian screen'''

    def read_completed_extractions(self):
        with open(self.completed_path, 'r') as f:
            completed_extractions = f.readlines()
            return completed_extractions

    def write_completed_extraction(self, completed_extraction_name):
        with open(self.completed_path, 'a') as f:
            f.write(completed_extraction_name)

    def run(self):
        self.root.deiconify()
        self.root.mainloop()
