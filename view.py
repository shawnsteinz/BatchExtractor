import tkinter.ttk as ttk
import tkinter as tk


class View:
    def __init__(self, master):
        self.tree = ttk.Treeview(master)
        self.sidePanel = SidePanel(master)
        self.tree["columns"] = "name"
        self.tree.column("name", width=200)
        self.tree.heading("name", text="Name")

        self.tree.insert("", 0, text="C:\downloads\GoT", values="Game_of_Thrones")
        self.tree.insert("", 0, text="C:\downloads\Suits", values="Suits")

        self.tree.pack()


class SidePanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.dicovery = tk.Button(self.frame, text="Discover")
        self.dicovery.pack(side="top", fill=tk.BOTH)
        self.extract = tk.Button(self.frame, text="Extract")
        self.extract.pack(side="top", fill=tk.BOTH)
