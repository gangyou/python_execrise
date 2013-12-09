import os, time
from shutil import *

def show_file_info(filename):
	stat_info = os.stat(filename)
	print '\tMode 	:', stat_info.st_mode
	print '\tCreated:', time.ctime(stat_info.st_ctime)
	print '\tAccess :', time.ctime(stat_info.st_atime)
	print '\tModified:', time.ctime(stat_info.st_mtime)

if not os.path.exists('example'): os.mkdir('example')
print 'SOURCE:'
show_file_info('shutil-copy2.py')
copy2('shutil-copy2.py', 'example')
print 'DEST:'
show_file_info('example/shutil-copy2.py')