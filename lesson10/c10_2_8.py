import logging

format = '%(levelname)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=format)

logging.info('info %s %s', 'test', 'test2')
