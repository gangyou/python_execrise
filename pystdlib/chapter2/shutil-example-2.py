import shutil, os

SOURCE = "samples"
BACKUP = "samples-bak"


# create a backup directory
shutil.copytree(SOURCE, BACKUP)

# shutil.copytree(SOURCE, BACKUP, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))

print os.listdir(BACKUP)

# remove it
shutil.rmtree(BACKUP)

print os.listdir(BACKUP)