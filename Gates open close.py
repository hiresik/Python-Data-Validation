    
import pandas as pd
import csv
import numpy as np
from datetime import datetime
import time
import re

r='C:\Docs\Lab 4\Data\SAP\Gate open close\Old\GAte_Open_close1.csv'
w='C:\Docs\Lab 4\Data\SAP\Gate open close\Old\GAte_Open_close1_out.csv'


with open(r, 'r') as source:
    with open(w, 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        # headers = reader.fieldnames()
        writer.writerow(['EVT_DISPLAY_NAME','FET_FLT_FLIGHT_NUMBER','FET_FLT_FLIGHT_DATE','FET_EVT_EVENT_CODE','FET_EVENT_TIME','FET_SEVERITY_CODE'])
        source.readline()
        for row in reader:
            # print row
            # ts0 = """+row[1]+"""
            ts = row[2]
            ts1 = row[4]
            # # ts2 = row[7]
            # # ts3 = row[8]
            # # ts4 = row[9]

           
            ts = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d")
            ts1 = datetime.strptime(ts1, '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d")

            # print ts
            
            # ts2 = datetime.strptime(ts2, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts3 = datetime.strptime(ts3, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts4 = datetime.strptime(ts4, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts5=str(ts4)
            # ts6 = ts5.replace("1975", "2075")
            # ts7 = datetime.strptime(ts6, "%Y-%m-%d").strftime("%Y-%m-%d")
                        
                
            # if ts != "" or ts1!= "":
            # #  # or ts1 != "" or ts2 !="" or ts3 !="" or ts4 !="" :
            # #     # row[1]=ts0
            # row[2] = ts 
            #     row[4] = ts1
            # #     # row[7] = ts2 
                # row[8] = ts3
                # row[9] = ts7  
            # if (ts<'2017-10-1'):
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