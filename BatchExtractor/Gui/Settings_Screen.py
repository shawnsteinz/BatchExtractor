from tkinter import filedialog
from tkinter import *


class Settings_Screen:

    def __init__(self, source, destination, shelve_handler):
        self.source = source
        self.destination = destination
        self.sh = shelve_handler

    def build_settings_screen(self):
        settings = Frame()
        Label(settings, text="Settings", font="TkDefaultFont 24 bold").grid(column=0,
                                                                            row=0, columnspan=4, sticky=NW, pady=5)
        Label(settings, text="Select source folder:").grid(column=0, row=1, pady=20, sticky=W)
        source_folder_entry = Entry(settings, textvariable=self.source, width=40)
        source_folder_entry.grid(column=1, row=1, sticky=W)
        browse_button = Button(settings, text="Browse...", command=self.select_source)
        browse_button.grid(column=4, row=1, sticky=W)

        Label(settings, text="Select folder to extract to:").grid(column=0, row=2, pady=20, sticky=W)
        destination_folder_entry = Entry(settings, textvariable=self.destination, width=40)
        destination_folder_entry.grid(column=1, row=2)
        browse_button2 = Button(settings, text="Browse...", command=self.select_destination)
        browse_button2.grid(column=4, row=2, sticky=W)

        back_button = Button(settings, text="Back", )
        back_button.grid(column=4, row=4, padx=10)

        return settings

    def select_source(self):
        source = filedialog.askdirectory()
        self.source.set(source)
        self.sh.set_setting('src', source)

    def select_destination(self):
        destination = filedialog.askdirectory()
        self.destination.set(destination)
        self.sh.set_setting('des', destination)
