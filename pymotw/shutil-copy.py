import os
from shutil import *

os.mkdir('example')
print 'BEFORE:', os.listdir('example')
copy('shutil-copy.py', 'example')
print 'AFTER:', os.listdir('example')