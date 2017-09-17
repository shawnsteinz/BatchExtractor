import tkinter.ttk as ttk
import tkinter as tk


class View:
    def __init__(self, master):
        self.tree = ttk.Treeview(master)
        self.sidePanel = SidePanel(master)
        self.tree["columns"] = "name"
        self.tree.column("name", width=1000)
        self.tree.heading("name", text="Name")
        self.tree['show'] = 'headings'
        self.tree.pack()

    def fill_tree(self, file_list):
        for item in file_list.files:
            self.tree.insert('', 'end', values=item.file_location)


class SidePanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.discover = tk.Button(self.frame, text="Discover")
        self.discover.pack(side="top", fill=tk.BOTH)
        self.extract = tk.Button(self.frame, text="Extract")
        self.extract.pack(side="top", fill=tk.BOTH)
