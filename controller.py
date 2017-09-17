from model import Files
from view import *
from tkinter import *


class Controller:
    def __init__(self, extract_dir, search_dir, location_7zip, location_completed_extractions):
        self.root = Tk()
        self.view = View(self.root)
        self.view.sidePanel.discover.bind("<Button>", self.discover)
        self.view.sidePanel.extract.bind("<Button>", self.extract)
        self.files = Files(extract_dir=extract_dir, search_dir=search_dir, location_7zip=location_7zip)
        self.location_completed_extractions = location_completed_extractions

    def discover(self, event):
        self.files.discovery(self.read_completed_file())
        self.view.fill_tree(self.files.files)

    def extract(self):
        for file in self.files.files:
            if file.extract() is True:
                self.write_completed_extraction(file.file_location)
                print('extracted a file')
            '''update progress bar and file in the main screen'''

    def write_completed_extraction(self, completed_extraction_name):
        with open(self.location_completed_extractions, 'a') as f:
            f.write(completed_extraction_name)

    def read_completed_file(self):
        with open(self.location_completed_extractions, 'r') as f:
            completed = []
            lines = f.readlines()
            for line in lines:
                completed.append(line.strip())
        return completed

    def run(self):
        self.root.deiconify()
        self.root.mainloop()
