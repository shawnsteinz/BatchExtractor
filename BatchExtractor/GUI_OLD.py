__author__ = 'Misja & Shawn'


from subprocess import *
from pickle import *
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from winsound import *
import os


class Finder:

    extensions = ('.rar', '.zip', '.7z')

    def __init__(self, origin, database):
        self.origin = origin
        self.database = database

    def find(self, origin):

        locations = []
        files = os.listdir(origin)

        for file in files:
            if file[-4:] in self.extensions:
                locations.append(origin + os.path.sep + file)
            elif os.path.isdir(origin + os.path.sep + file):
                new_files = self.find(origin + os.path.sep + file)
                if new_files:
                    for new_file in new_files:
                        locations.append(new_file)

        return locations

    def get_locations(self):
        locations = self.find(self.origin)
        return self.filter(locations)

    def filter(self, locations):

        completed = load(open(self.database, 'rb'))
        filtered_list = []
        for file in locations:
            if file not in completed:
                filtered_list.append(file)
        return filtered_list


class Command:

    def __init__(self, destination, locations, database):
        self.destination = destination
        self.commands = self.prepare(locations)
        self.completed = []
        self.database = database

    def prepare(self, locations):
        commands = []

        for origin in locations:
            command = ['7z x -aos %s -o' % origin + self.destination, origin]
            commands.append(command)

        return commands

    def execute(self):
        """
        nummer = 100 / self.commands.__sizeof__()
        print(nummer)
        """

        for command in self.commands:
            return_value = call(command[0], shell=True)

            if return_value == 0:
                self.completed.append(command[1])

        x = load(open(self.database, 'rb'))
        dump(x + self.completed,  open(self.database, 'wb'))


class Gui:

    def __init__(self, root):
        self.source = StringVar()
        self.destination = StringVar()
        self.database = StringVar()
        self.root = root
        self.build_gui()

    def build_gui(self):

        c = (N, W, S, E)
        self.root.title("")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        frame = ttk.Frame(padding="4")
        frame.grid(column=0, row=0, sticky=c)
        '''frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=0)
        frame.columnconfigure(3, weight=0)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)'''

        ttk.Label(frame, text="BatchExtractor", font="TkDefaultFont 24 bold").grid(column=0,
                                                                                     row=0, columnspan=4, sticky=NW, pady=5)
        ttk.Label(frame, text="Select source folder:").grid(column=0, row=1, pady=20, sticky=W)
        source_folder_entry = ttk.Entry(frame, textvariable=self.source, width=40)
        source_folder_entry.grid(column=1, row=1, sticky=W)
        browse_button = ttk.Button(frame, text="Browse...", command=self.select_source)
        browse_button.grid(column=4, row=1, sticky=W)

        ttk.Label(frame, text="Select folder to extract to:").grid(column=0, row=2, pady=20, sticky=W)
        destination_folder_entry = ttk.Entry(frame, textvariable=self.destination, width=40)
        destination_folder_entry.grid(column=1, row=2)
        browse_button2 = ttk.Button(frame, text="Browse...", command=self.select_destination)
        browse_button2.grid(column=4, row=2, sticky=W)

        ttk.Label(frame, text="Select database.py file:").grid(column=0, row=3, pady=20, sticky=W)
        database_file_entry = ttk.Entry(frame, textvariable=self.database, width=40)
        database_file_entry.grid(column=1, row=3, sticky=EW)
        browse_button3 = ttk.Button(frame, text="Browse...", command=self.select_database)
        browse_button3.grid(column=4, row=3, sticky=W)

        self.progressbar = ttk.Progressbar(frame, orient=HORIZONTAL, mode='determinate', maximum=100)
        self.progressbar.grid(column=0, row=4, columnspan=3, sticky=EW)

        start_button = ttk.Button(frame, text="Start", command=lambda: self.start(self.source, self.destination, self.database))
        start_button.grid(column=4, row=4, padx=10)

    def select_source(self):
        self.source.set(filedialog.askdirectory())

    def select_destination(self):
        self.destination.set(filedialog.askdirectory())

    def select_database(self):
        self.database.set(filedialog.askopenfilename())

    def run_progressbar(self, number):
        self.progressbar.step([number])

    def play_sound(self):
        PlaySound("wait_music.wav", SND_ASYNC)


    @property
    def get_source(self):
        return self.source

    @property
    def get_destination(self):
        return self.destination

    @property
    def get_database(self):
        return self.database

    def start(self, source_folder, destination_folder, database_file):
        source_folder = source_folder.get()
        destination_folder = destination_folder.get()
        database_file = database_file.get()
        if os.path.isdir(source_folder):
            if os.path.isdir(destination_folder):
                if os.path.isfile(database_file):
                    self.play_sound()
                    finder = Finder(source_folder, database_file)
                    command = Command(destination_folder, finder.get_locations(), database_file)
                    command.execute()
                else:
                    print("database.py is not given")
            else:
                print("destination is not given")
        else:
            print("source is not given")


class Model():

    def __init__(self):
        self.source_folder = str()
        self.destination_folder = str()
        self.database_file = str()

    def main(self):
        root = Tk()
        Gui(root)
        root.mainloop()


if __name__ == '__main__':
    Model().main()









