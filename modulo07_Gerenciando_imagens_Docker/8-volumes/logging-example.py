#!/usr/bin/env python3 

import os
import sys
import time
import logging
import logging.config

LOGFILE = os.getenv('LOGFILE', 'example.log')

# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{LOGFILE}',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console','file'],
            'propagete': True,
        },
    },
})

logger = logging.getLogger('')
level = logging.getLevelName('DEBUG')
logger.setLevel(level)

count = 1
count_end = int(os.getenv('COUNT_END', 10))
sleep_time = 1
while count <= count_end:
    msg = f'Count is {count}'
    logger.info(msg)
    count+=1
    time.sleep(sleep_time)

    
    