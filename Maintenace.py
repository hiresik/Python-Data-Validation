
import pandas as pd
import csv
import numpy as np
from datetime import datetime
import time
import re

r='C:\Docs\Lab 4\Data\SAP\User Story Data 11042018\Working copy\Maintenance_18032018.csv'
w='C:\Docs\Lab 4\Data\SAP\User Story Data 11042018\Working copy\Maintenance_18032018_out.csv'


with open(r, 'r') as source:
    with open(w, 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        # headers = reader.fieldnames()
        writer.writerow(['PACKAGE_ID','PACKAGE_STATUS','LOC','LOC_DESCRIPTION','GEO_LOC','AIRCRAFT','PKG_TYPE','PKG_TYPE_DESCRP','PLANNED_START_DATE','PLANNED_END_DATE','ACTUAL_START_DATE','ACTUAL_END_DATE'])
    
        source.readline()
        for row in reader:
            # print row
            # ts0 = """+row[1]+"""
            ts = row[8]
            ts1 = row[9]
            # ts2 = row[7]
            # ts3 = row[8]
            # ts4 = row[9]

            if len(ts) >9:          
                ts = datetime.strptime(ts, '%m/%d/%Y %I:%M:%S %p').strftime("%Y-%m-%d %H:%M:%S")
            else:
                ts = datetime.strptime(ts, '%m/%d/%Y').strftime("%Y-%m-%d %H:%M:%S")

            ts1 = datetime.strptime(ts1, '%m/%d/%Y %I:%M:%S %p').strftime("%Y-%m-%d %H:%M:%S")

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
            row[8] = ts 
            row[9] = ts1
            #     # row[7] = ts2 
                # row[8] = ts3
                # row[9] = ts7  
            # if ts>='2018-02-28' and ts<='2018-03-01':
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