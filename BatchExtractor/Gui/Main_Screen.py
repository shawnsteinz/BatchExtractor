from tkinter import *
import BatchExtractor.Main
import tkinter.ttk as ttk



class Main_Screen:
    def __init__(self, sh, files):
        self.var = int()
        self.v = StringVar()
        self.sh = sh
        self.files = files
        self.label = []
        self.checkbutton = []


    def build_main_screen(self):
        self.main_screen = Frame()
        canvas = Canvas(self.main_screen, bg="black")
        self.frame = Frame(canvas, bg="black", relief=SUNKEN)
        scrollbar = Scrollbar(self.main_screen, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=N + S + W)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.fill_frame()
        start_button = Button(self.main_screen, text="Start", height='2', width='10', command=self.run)
        start_button.grid(row=1, column=1, padx=(20, 0), pady=(10, 0))
        self.progressbar = ttk.Progressbar(self.main_screen, orient='horizontal', mode='determinate')
        self.progressbar.grid(row=1, column=0, sticky=W + E, padx=(1, 0), pady=(0, 0))

        def resize_to_window(event):
            size = (self.frame.winfo_reqwidth(), self.frame.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.frame.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=self.frame.winfo_reqwidth())

        self.frame.bind('<Configure>', resize_to_window)
        return self.main_screen

    def fill_frame(self):

        self.label = ["label%.d" % i for i in range(self.files.files.__len__())]
        self.checkbutton = ["checkbutton%.d" % i for i in range(self.files.files.__len__())]
        self.Name = Label(self.frame, text="Name", bg="black", fg='green', width=80, anchor=W)
        self.Name.grid(row=0, column=0, sticky=W)
        self.Extract = Label(self.frame, text="Extract", bg="black", fg='green', width=7, anchor=W)
        self.Extract.grid(row=0, column=1, sticky=W)
        for file in self.files.files:
            for id in range(self.label.__len__()):
                self.var += 1
                self.label[id] = Label(self.frame, text=file.location, bg="black", fg='green')
                self.label[id].grid(row=self.var, column=0, sticky=W)
                self.checkbutton[id] = Checkbutton(self.frame, variable=self.var, bg="black")
                self.checkbutton[id].grid(row=self.var, column=1, sticky=W)

    def clear_frame(self):
        self.var = 1
        for id in range(self.label.__len__()):
            self.label[id].grid_forget()
            self.checkbutton[id].grid_forget()


    def run(self):
        """self.progressbar.start(50)"""
        BatchExtractor.Main.Main().extract()
        self.clear_frame()






