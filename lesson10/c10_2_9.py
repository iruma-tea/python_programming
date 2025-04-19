import logging

format = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=format)

logging.info('info %s %s', 'test', 'test2')
