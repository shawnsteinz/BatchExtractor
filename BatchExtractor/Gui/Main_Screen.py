from tkinter import *
import BatchExtractor.Main
import BatchExtractor.Controller.Database
from BatchExtractor.Model.File import FileList
import tkinter.ttk as ttk


class Main_Screen:
    def __init__(self, sh):
        self.var = int()
        self.v = StringVar()
        self.sh = sh
        self.files = FileList(self.sh.get_setting('src'), self.sh.get_setting('ext'))
        self.files.remove_files_by_tasks(self.sh.get_excluded(), self.sh.get_completed())

    def build_main_screen(self):
        main_screen = Frame()
        canvas = Canvas(main_screen, bg="black")
        self.frame = Frame(canvas, bg="black", relief=SUNKEN)
        scrollbar = Scrollbar(main_screen, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=N + S + W)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.fill_frame()
        start_button = Button(main_screen, text="Start", height='2', width='10', command=self.run)
        start_button.grid(row=1, column=1, padx=(20, 0), pady=(10, 0))
        self.progressbar = ttk.Progressbar(main_screen, orient='horizontal', mode='determinate')
        self.progressbar.grid(row=1, column=0, sticky=W + E, padx=(1, 0), pady=(0, 0))

        def resize_to_window(event):
            size = (self.frame.winfo_reqwidth(), self.frame.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.frame.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=self.frame.winfo_reqwidth())

        self.frame.bind('<Configure>', resize_to_window)
        return main_screen

    def fill_frame(self):
        self.Name = Label(self.frame, text="Name", bg="black", fg='green', width=80, anchor=W)
        self.Name.grid(row=0, column=0, sticky=W)
        self.Extract = Label(self.frame, text="Extract", bg="black", fg='green', width=7, anchor=W)
        self.Extract.grid(row=0, column=1, sticky=W)
        for file in self.files.get_files():
            self.var += 1
            l = Label(self.frame, text=file.location, bg="black", fg='green')
            l.grid(row=self.var, column=0, sticky=W)
            b = Checkbutton(self.frame, variable=self.var, bg="black")
            b.grid(row=self.var, column=1, sticky=W)


    def rebuild(self):
        self.var = 0
        self.files = FileList(self.sh.get_setting('src'), self.sh.get_setting('ext'))
        self.files.remove_files_by_tasks(self.sh.get_excluded(), self.sh.get_completed())
        self.fill_frame()


    def run(self):
        self.progressbar.start(50)
        BatchExtractor.Main.Main().extract()
        self.rebuild()




