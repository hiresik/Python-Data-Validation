
import pandas as pd
import csv
import numpy as np
from datetime import datetime
import time
import re

r='C:\\Users\\S731377\\Documents\\LAB4\\SAP\\StandEvolution\\000000_0.csv'
w='C:\\testAutomation\\Hermes\\Lab4\\output\\output.csv'


# with open(r, 'r') as source:
#     with open(w, 'w') as result:
#         writer = csv.writer(result, lineterminator='\n')
#         reader = csv.reader(source)
        # headers = reader.fieldnames()
colnames=['Airline', 'Flight Number',    'FlightDate',  'Arr-Dep Flag', 'Old Bay',  'New Bay',  'Current Gate', 'Change Date']

df = pd.read_csv('C:\\Users\\S731377\\Documents\\LAB4\\SAP\\StandEvolution\\000000_0.csv', names=colnames, header=None)
#print df['Flight Date'].to_string(index=False)
df['FlightDate'] = pd.to_datetime(df['FlightDate'].to_string(index=False))
#print pd.to_datetime(pd.Series(df.FlightDate))
print df['FlightDate'].dt.date()


#ts = datetime.strptime(ts, '%Y-%m-%d %H:%M').strftime("%Y-%m-%d")
#print ts

        # writer.writerow(['Airline', 'Flight Number',    'Flight Date',  'Arr-Dep Flag', 'Old Bay',  'New Bay',  'Current Gate', 'Change Date'])
        #
        # source.readline()
        # for row in reader:
            # print row
            # ts0 = """+row[1]+"""
            # ts = row[2]
            # # ts1 = row[7]
            # # ts2 = row[7]
            # # ts3 = row[8]
            # # ts4 = row[9]
            #
            # if (ts != '\N') :
            #     ts = datetime.strptime(ts, '%Y-%m-%d %H:%M').strftime("%Y-%m-%d")
            # else:
            #     print "Invalid datetime" , ts
            #     ts = datetime.strptime(ts, '%Y-%m-%d %H:%M').strftime("%Y-%m-%d")
            #
            # print ts
            
            # ts2 = datetime.strptime(ts2, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts3 = datetime.strptime(ts3, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts4 = datetime.strptime(ts4, '%d-%b-%y').strftime("%Y-%m-%d")
            # ts5=str(ts4)
            # ts6 = ts5.replace("1975", "2075")
            # ts7 = datetime.strptime(ts6, "%Y-%m-%d").strftime("%Y-%m-%d")
                        
                
            # if ts != "" or ts1 != "" or ts2 !="" or ts3 !="" or ts4 !="" :
            #     # row[1]=ts0
            #     # row[2] = ts
            #     # row[7] = ts1
            #     # row[7] = ts2
            #     # row[8] = ts3
            #     # row[9] = ts7
            # if (ts>='2017-01-01'):
            #     writer.writerow(row)


# source.close()
# result.close()
#
# count = 0
# with open(r, 'rb') as count_file:
#     csv_reader = csv.reader(count_file)
#     for row in csv_reader:
#         count += 1
#
# print "Source Count ", count
#
# aftermerge = 0
# with open(w, 'rb') as count_file:
#     csv_reader = csv.reader(count_file)
#     for row in csv_reader:
#         aftermerge += 1
#
# print "Output count ",aftermerge