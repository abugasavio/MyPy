import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s  %(levelname)s: %(message)s", filename='log.log')

logging.debug('This message will be ignored')
logging.info('This should be logged')
logging.warning('And this, too')
