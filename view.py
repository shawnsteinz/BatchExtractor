
import tkinter.ttk as ttk


class View:
    def __init__(self, master):
        tree = ttk.Treeview(master)

        tree["columns"] = "name"
        tree.column("name", width=200)
        tree.heading("name", text="Name")

        tree.insert("", 0, text="C:\downloads\GoT", values="Game_of_Thrones")
        tree.insert("", 0, text="C:\downloads\Suits", values="Suits")

        tree.pack()
