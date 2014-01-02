import logging
from pprint import pformat
from pprint_data import data

logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s %(levelname)-8s %(message)s',)

logging.debug('Loggin pformatted data')
logging.debug(pformat(data))