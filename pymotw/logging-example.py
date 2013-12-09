import logging

LOG_FILENAME = '/tmp/logging_example.out'
logging.basicConfig(filename=LOG_FILENAME, level = logging.DEBUG)

logging.debug("This message should go to the log file")

import fileinput

for line in fileinput.input(LOG_FILENAME):
	print line