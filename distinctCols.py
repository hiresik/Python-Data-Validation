

import pandas as pd
import pandasql as pds
import csv
import numpy as np
np.set_printoptions(threshold=np.nan)


w='C:\Docs\Lab 4\Data\SAP\ULD scanning\ULD Scanning Masked Formatted\ULD Scanning_001_Aug17_DEC17_JAN18_FEB18_Masked_EKonly.csv'




df=pd.read_csv(w)
# df=pd.read_excel(w)
# df = pd.read_csv('C:\Docs\Lab 4\Data\SAP\FlightMovementType\Oct 2017.csv', header=None, usecols=[2])
# print df['DEP_DATE'].unique()

# q1 = """select distinct Date from df"""
# print "starting sql....."
# print pds.sqldf(q1, locals())
shor = df['FLIGHTDATE'].str.slice(0,10)
# print "ending sql....."

print shor.unique()

# print df.groupby(['FLIGHTDATE']).count()

# grp = df.groupby['Date']
# grp.describe()

# gb = df.groups
# gb.keys()

# key_list_from_gb = [key1, key2, key3]

# for key, values in gb.iteritems():
#     if key in key_list_from_gb:
#         print df.ix[values], "\n"
aftermerge = 0
with open(w, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        aftermerge += 1

print "Output count ",aftermerge