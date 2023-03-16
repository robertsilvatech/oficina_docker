#!/usr/bin/env python3 

import time
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(process)d - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

count = 0 
count_end = 10
sleep_time = 2
while count < count_end:
    msg = f'Count is {count}'
    logging.info(msg)
    print(msg)
    count+=1
    time.sleep(sleep_time)

    
    