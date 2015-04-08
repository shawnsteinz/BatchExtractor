__author__ = 'Misja'

from BatchExtractor.database import ShelveHandler

sh = ShelveHandler()
sh.set_completed([])
sh.set_excluded([])
sh.set_setting('src', 'E:\\Test\\SRC')
sh.set_setting('des', 'E:\\Test\\DES')
sh.set_setting('ext', ['.rar', '.zip', '.7z'])


sh = ShelveHandler()
print(sh.get_completed())
print(sh.get_setting('ext'))
