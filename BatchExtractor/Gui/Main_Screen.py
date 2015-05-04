from tkinter import *
import BatchExtractor.Main
import tkinter.ttk as ttk
import tkinter.font as tkFont



class Main_Screen:
    def __init__(self, sh, files):
        self.var = int()
        self.v = StringVar()
        self.sh = sh
        self.files = files
        self.label = []
        self.checkbutton = []
        self.list_header = ['Name', 'size']
        self.data_list = []
        self.fill_data_list()
        self.tree = None

    def build_main_screen(self):
        main_screen  = ttk.Frame()
        container = ttk.Frame(main_screen)
        container.grid(column=0, row=0)

        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=self.list_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self._build_tree()

        start_button = Button(main_screen, text="Start", height='2', width='10', command=self.run)
        start_button.grid(row=1, column=1, padx=(20, 0), pady=(10, 0))
        self.progressbar = ttk.Progressbar(main_screen, orient='horizontal', mode='determinate')
        self.progressbar.grid(row=1, column=0, sticky=W + E, padx=(1, 0), pady=(0, 0))

        return main_screen

    def _build_tree(self):
        for col in self.list_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: self.sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in self.data_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(self.list_header[ix],width=None)<col_w:
                    self.tree.column(self.list_header[ix], width=col_w)

    def sortby(self, tree, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
        # if the data to be sorted is numeric change to float
        #data =  change_numeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: self.sortby(tree, col, \
            int(not descending)))

    def fill_data_list(self):
        print("hey")



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
        """self.clear_frame()"""






