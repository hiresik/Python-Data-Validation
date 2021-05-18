
import pandas as pd
import csv
import numpy as np
from datetime import datetime
import time
import re

r='C:\Docs\Lab 4\Data\SAP\PAX Forecast\PAX Forecast_28032018.csv'
w='C:\Docs\Lab 4\Data\SAP\PAX Forecast\PAX Forecast_28032018_out.csv'


with open(r, 'r') as source:
    with open(w, 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        # headers = reader.fieldnames()
        writer.writerow(['CARR_CODE','FLT_NO','ORGN','DSTN','CLS_MASTER_COMP','Date','REC_TYPE','DCP1','DCP2','DCP3','DCP4','DCP5','DCP6','DCP7','DCP8','DCP9','DCP10','DCP11','DCP12','DCP13','DCP14','DCP15','DCP16','DCP17','DCP18','DCP19','DCP20','DCP21','DCP22','DCP23','DCP24'])
    
        source.readline()
        for row in reader:
            # print row
            # ts0 = """+row[1]+"""
            ts = row[5]
            # ts1 = row[4]
            # ts2 = row[7]
            # ts3 = row[8]
            # ts4 = row[9]

           
            # ts = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.0%f').strftime("%Y-%m-%d")
            # ts1 = datetime.strptime(ts1, '%Y-%m-%d %H:%M:%S.0%f').strftime("%Y-%m-%d")

            # print ts
            
            # ts2 = datetime.strptime(ts2, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts3 = datetime.strptime(ts3, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts4 = datetime.strptime(ts4, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts5=str(ts4)
            # ts6 = ts5.replace("1975", "2075")
            # ts7 = datetime.strptime(ts6, "%Y-%m-%d").strftime("%Y-%m-%d")
                        
                
            # if ts != "":
            #  # or ts1 != "" or ts2 !="" or ts3 !="" or ts4 !="" :
            #     # row[1]=ts0
            #     row[3] = ts 
            #     row[4] = ts1
            #     # row[7] = ts2 
                # row[8] = ts3
                # row[9] = ts7  
            if ts>='2018-02-28' and ts<='2018-03-01':
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