#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
        python script!"""

__author__ = "Zsolt Laszlo"
__copyright__ = "Copyright 2016"
__credits__ = ["Zsolt Laszlo"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Zsolt Laszlo"
__email__ = "lzsolti1970@gmail.com"
__status__ = "Development"

import csv
from pymodbus3.client.sync import ModbusTcpClient
from pathlib import Path
import time

my_file = Path("velebit.csv")
fieldnames = ['PT-101',
              'PT-103',
              'PT-104',
              'TT-101',
              'TT-102',
              'TT-103',
              'TT-104',
              'TT-105',
              'TT-106',
              'TT-107',
              'TT-501',
              'FIT-101',
              'PT-501',
              'XT-501',
              'XT-502',
              'XT-503',
              'PT-201',
              'TT-201',
              'PT-151',
              'PT-152',
              'PT-251',
              'TT-151',
              'TT-451',
              'TT-251',
              'TT-452',
              'TT-453',
              'TT-454',
              'TT-455',
              'ST-551',
              'TIME']

client = ModbusTcpClient('127.0.0.1')
dfdata = {}
result = client.read_holding_registers(121, 29)
localtime = time.asctime( time.localtime(time.time()) )
for j in range(0, len(result.registers)):
    result.registers[j] = result.registers[j] / float(10)
    dfdata[fieldnames[j]] = result.registers[j]

dfdata[fieldnames[28]] = localtime
client.close()
if my_file.exists():
    fileExist = True
else:
    fileExist = False

if fileExist == False:
    with open('velebit.csv', 'w') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(dfdata)

else:
    with open('velebit.csv', 'a') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(dfdata)

