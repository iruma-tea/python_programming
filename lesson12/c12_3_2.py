import concurrent.futures
import logging
import time

import concurrent


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        f1 = executor.submit(workder, 2, 5)
        f2 = executor.submit(workder, 2, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())


def workder(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r


if __name__ == '__main__':
    main()
