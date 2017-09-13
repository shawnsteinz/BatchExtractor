from BatchExtractor.Database.Database import ShelveHandler
from BatchExtractor.Model.File import FileList
from BatchExtractor.Model.Task import TaskHandler

sh = ShelveHandler('D:\\Test\\DB\\Shelve')
sh.set_setting('src', 'D:\\Test\\SRC')
sh.set_setting('des', 'D:\\Test\\DES')
sh.set_setting('ext', ['.rar', '.zip', '.7z'])

excluded = sh.get_excluded()
completed = sh.get_completed()

fl = FileList(sh.get_setting('src'), sh.get_setting('ext'))
fl.remove_files_by_tasks(sh.get_excluded(), sh.get_completed())
th = TaskHandler(fl.get_files(), sh.get_setting('des'))
th.execute_tasks()
sh.set_completed(th.successful_tasks)


sh = ShelveHandler('D:\\Test\\DB\\Shelve')

for task in sh.get_completed():
    print('Task %s || %s || %s' % (task.file.location, task.destination_directory, task.file.get_size()))