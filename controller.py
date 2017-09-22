from model import ArchiveFinder
from view import *
from tkinter import *
from utilities import write, read, extract
from constants import *

'''Controller'''


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
        files_to_skip = read(self.log_file_name)
        self.found_archives = self.finder.search(files_to_skip)
        self.__update_tree()

    def __update_tree(self):
        self.view.fill_tree(self.found_archives)
        self.root.update()

    def __update_archive(self, archive):
        for i, value in enumerate(self.found_archives):
            if value.file_name == archive.file_name:
                self.found_archives[i] = archive
                self.__update_tree()

    def extract(self, event):
        for archive in self.found_archives:
            archive.status = EXTRACTING
            self.__update_archive(archive)
            result = extract(archive.file_name, self.extract_dir)

            if result['status']:
                write(self.log_file_name, archive.file_name)
                archive.status = COMPLETED
                self.__update_archive(archive)
            else:
                archive.status = FAILED
                write(self.error_log_file_name, result['msg'])
                self.__update_archive(archive)

    def exclude(self, event):
        file_name = ''
        for i, value in enumerate(self.found_archives):
            if file_name == value.file_name:
                self.found_archives.pop(i)
                write(self.error_log_file_name, file_name)

    def run(self):
        self.root.deiconify()
        self.root.geometry("%dx%d" % (1600, 600))
        self.root.title('BatchExtractor')
        self.root.mainloop()
