from BatchExtractor.Model.File import FileList
from BatchExtractor.Model.Task import TaskHandler
import BatchExtractor.Gui.Gui_Builder
from BatchExtractor.Controller.Database import ShelveHandler

class Main():

    def __init__(self):
        self.sh = ShelveHandler('D:\\Test\\Shelve')
        self.sh.set_setting('src', 'D:\\Test\\SRC')
        self.sh.set_setting('des', 'D:\\Test\\DES')
        self.sh.set_setting('ext', ['.rar', '.zip', '.7z'])

    def main(self):
        BatchExtractor.Gui.Gui_Builder.Gui(self.sh).start()

    def extract(self):

        fl = FileList(self.sh.get_setting('src'), self.sh.get_setting('ext'))
        fl.remove_files_by_tasks(self.sh.get_excluded(), self.sh.get_completed())
        th = TaskHandler(fl.get_files(), self.sh.get_setting('des'))
        th.execute_tasks()
        self.sh.set_completed(th.successful_tasks)

if __name__ == '__main__':
    Main().main()
