
import pandas as pd
import csv
import numpy as np
from datetime import datetime
import time
import re

r='C:\Docs\Lab 4\Data\SAP\ULD scanning\ULD Scanning_001.csv'
w='C:\Docs\Lab 4\Data\SAP\ULD scanning\ULD Scanning Masked Formatted\ULD Scanning_001_Aug17_DEC17_JAN18_FEB18_Masked_EKonly_out.csv'

with open(r, 'r') as source:
    with open(w, 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        # headers = reader.fieldnames()
        writer.writerow(['FLIGHTDATE',  'FLIGHTNUMBER', 'A/D',  'STA/D',    'ETA/D',    'ATA/D',    'BAY',  'GATE', 'ULDTYPE',  'PRODUCT',  'CLASS',    'ULDNO',    'ACTION',   'ActionTime',   'ScannedBy_StaffID',    'ScannedBy_StaffName',  'Location'])
    
        source.readline()
        for row in reader:
            # print row
            # ts0 = """+row[1]+"""
            ts = row[0]
            ts1 = row[2]
            # ts2 = row[7]
            # ts3 = row[8]
            # ts4 = row[9]

           
            # ts = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            # ts1 = datetime.strptime(ts1, '%d-%b-%Y %H%M').strftime('%Y-%m-%d %H:%M')
       
                # ts = datetime.strptime(ts, '%Y-%m-%d %H:%M').strftime("%Y-%m-%d")

            # print ts
            
            # ts2 = datetime.strptime(ts2, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts3 = datetime.strptime(ts3, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts4 = datetime.strptime(ts4, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts5=str(ts4)
            # ts6 = ts5.replace("1975", "2075")
            # ts7 = datetime.strptime(ts6, "%Y-%m-%d").strftime("%Y-%m-%d")
                        
                
            # if ts != "":
             # or ts1 != "" or ts2 !="" or ts3 !="" or ts4 !="" :
                # row[1]=ts0
            # row[0] = ts
            # row[7] = ts1
            # row[7] = ts2 
            # row[8] = ts3
            # row[9] = ts7  
            # if len(ts) == 6:
            dt = ts[0:7]
                # print dt
            # else:
                # dt = ""
            # print ts
            if (dt=='2017-08' and ts1=='D'):
                print row
                writer.writerow(row) 
          


source.close()
result.close()

count = 0
with open(r, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1

print "Source Count ", count

aftermerge = 0
with open(w, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        aftermerge += 1

print "Output count ",aftermerge