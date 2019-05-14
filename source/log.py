#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging, os
from datetime import datetime


class Loger:

    def logger():
        logging.basicConfig(filename='logs\app.log', level=logging.INFO)
        logging.info('Started')
        main.do_log()
        logging.info('Finished')

    def writeLog(status):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\logs\\app.log'
        # os.chdir(ROOT_DIR)

        logging.basicConfig(filename=ROOT_DIR, format='%(asctime)s %(message)s',
                            datefmt=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logging.warning(status)


if __name__ == '__main__':
    logger()
