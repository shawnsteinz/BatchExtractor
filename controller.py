from model import ArchiveFinder
from view import *
from tkinter import *
from utilities import write, read, extract


class Controller:
    def __init__(self, extract_dir, search_dir, log_file_name, error_log_file_name):
        self.extract_dir = extract_dir
        self.finder = ArchiveFinder(search_dir)
        self.found_archives = []
        self.log_file_name = log_file_name
        self.error_log_file_name = error_log_file_name
        self.root = Tk()
        self.view = View(self.root)
        self.view.sidePanel.search.bind("<Button>", self.search)
        self.view.sidePanel.extract.bind("<Button>", self.extract)

    def search(self, event):
        files_to_skip = read(file_name=self.log_file_name)
        self.found_archives = self.finder.search(files_to_skip)
        self.view.fill_tree(self.found_archives)

    def extract(self, event):
        for archive in self.found_archives:
            result = extract(archive.file_name, self.extract_dir)
            if result['status']:
                write(self.log_file_name, archive.file_name)
                return result
            else:
                write(self.error_log_file_name, result['msg'])
                return result

    def run(self):
        self.root.deiconify()
        self.root.mainloop()
