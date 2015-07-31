#!/usr/bin/python

import logging

LOG_FILENAME = '../doCI.log'
FORMAT = '%(asctime)-15s %(message)s'

logging.basicConfig(format=FORMAT,filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger('CI')

logger.info("running CI..")

