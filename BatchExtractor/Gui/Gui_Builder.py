from tkinter import *
from tkinter import ttk
import BatchExtractor.Gui.Settings_Screen
import BatchExtractor.Gui.Main_Screen


class Gui_Builder:
    def __init__(self, sh, file):
        self.root = Tk()
        self.sh = sh
        self.source = StringVar()
        self.source.set(self.sh.get_setting('src'))
        self.destination = StringVar()
        self.destination.set(self.sh.get_setting('des'))
        self.database = StringVar()
        self.file = file
        self.build_gui()

    def build_gui(self):
        self.root.geometry("%dx%d" % (800, 600))
        self.root.title('BatchExtractor')

        nb = ttk.Notebook(self.root)
        nb.pack(fill='both', expand='yes')

        main = BatchExtractor.Gui.Main_Screen.Main_Screen(self.sh, self.file).build_main_screen()
        settings_window = BatchExtractor.Gui.Settings_Screen.Settings_Screen(self.source, self.destination,
                                                                             self.sh).build_settings_screen()

        nb.add(main, text='Main')
        nb.add(settings_window, text='Settings')

    def start(self):
        self.root.mainloop()


