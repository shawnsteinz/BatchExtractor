from tkinter import *
import BatchExtractor.Main
import BatchExtractor.Controller.Database
from BatchExtractor.Model.File import FileList

class Main_Screen:

    def __init__(self, sh):
        self.sh = sh
        self.files = FileList(self.sh.get_setting('src'), self.sh.get_setting('ext'))

    def build_main_screen(self):

        main_screen = Frame()

        self.listbox = Listbox(main_screen, width=80, height=20, bg="black", fg='green')
        self.listbox.grid(row=0, column=0, sticky=W, pady=(30, 0), padx=(0, 20))
        print(self.files.get_files())
        for item in self.files.get_files():
                self.listbox.insert(END, item)

        start_button = Button(main_screen, text="Start", height='2', width='10', command=self.run)
        start_button.grid(row=1, column=1, sticky=E, padx=(50, 0))

        return main_screen

    def run(self):
        BatchExtractor.Main.Main().extract()
        self.listbox.delete(0, END)

