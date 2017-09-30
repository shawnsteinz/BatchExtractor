import tkinter.ttk as ttk
import tkinter as tk

'''View'''


class View:
    def __init__(self, master):

        style = ttk.Style()
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.configure(".", font=('Helvetica', 8))
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                    ("Custom.Treeheading.text", {'sticky': 'we'})
                ]})
            ]}),
        ])

        style.configure("Custom.Treeview.Heading",
                        background="#383838", foreground="white", relief="ridge")
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        ttk.Style().configure("Custom.Treeview", background="#383838",
                              foreground="white")
        container = ttk.Frame(master)
        container.pack(side='top', fill='both', expand=True)

        self.list_header = ['Name']
        self.tree1 = ttk.Treeview(columns=self.list_header, show="headings", style="Custom.Treeview")
        self.tree1.heading("Name", text="Name")

        self.tree = ttk.Treeview(columns='status', style="Custom.Treeview")
        self.tree.heading('#0', text='Name')
        self.tree.heading('#1', text='Status')
        self.tree.column('#1', stretch='yes')
        self.tree.column('#0', stretch='yes')
        self.sidePanel = SidePanel(master)
        self.progressbar = Progressbar(master)
        self.sidePanel.frame.pack(side="right", fill="x", expand=False)
        self.progressbar.frame.pack(side="top", fill="x", expand=False)
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

    def fill_tree(self, files):

        self.clear_tree()

        for item in files:
            self.tree.insert('', 'end', text=item.display_name,
                             values=(item.status, item))

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)


class SidePanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.search = tk.Button(self.frame, text="Discover", relief='raised')
        self.search.pack(side='left', fill='both')
        self.extract = tk.Button(self.frame, text="Extract", relief='raised')
        self.extract.pack(side='left', fill='both')


class Progressbar:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.progressbar = ttk.Progressbar(self.frame, orient='horizontal', mode='determinate')
        self.progressbar.pack(side='left', fill='both', expand=True)
