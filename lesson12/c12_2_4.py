import logging
import multiprocessing


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == '__main__':
    with multiprocessing.Pool(5) as p:
        p1 = p.apply_async(worker1, (100,))
        logging.debug('executed')
        logging.debug(p1.get())
