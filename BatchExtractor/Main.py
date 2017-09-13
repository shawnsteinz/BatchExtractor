import BatchExtractor.Gui.Gui_Builder
from BatchExtractor.Database.Database import ShelveHandler
from BatchExtractor.Model.File import FileList
from BatchExtractor.Model.Task import TaskHandler


class Main():

    def __init__(self):
        self.sh = ShelveHandler('C:\\BE\\DB\\Shelve')
        self.sh.set_setting('src', 'C:\\BE\\Test\\SRC')
        self.sh.set_setting('des', 'C:\\BE\\Test\\DES')
        self.sh.set_setting('ext', ['.rar', '.zip', '.7z'])
        self.fl = FileList(self.sh.get_setting('src'), self.sh.get_setting('ext'))
        self.fl.remove_files_by_tasks(self.sh.get_excluded(), self.sh.get_completed())

    def main(self):
        BatchExtractor.Gui.Gui_Builder.Gui_Builder(self.sh, self.fl).start()

    def extract(self):


        th = TaskHandler(self.fl.get_files(), self.sh.get_setting('des'))
        th.execute_tasks()
        self.sh.set_completed(th.successful_tasks)


if __name__ == '__main__':
    Main().main()
