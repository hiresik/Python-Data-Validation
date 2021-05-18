import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime, date, time, timedelta
import time
import string
import unittest


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

''' Read the output file from Solver'''
df = pd.read_csv(ROOT_DIR+"\\"+sys.argv[1])

'''Filter the Solver output on the basis of Destination Airport'''
airPortValue = df.loc[df['destAirportID'] == sys.argv[2]]

''' Sort the output by flightNumber and store the result in output flight schedule file'''
sortedValue = airPortValue.sort_values(by=['operationDate'])

sortedValue.to_csv('output/curfew_flight_schedule.csv')

''' Read the Curfew rules and map it to the particular Airport
 and find the curfew time for a particular airport'''
df = pd.read_csv(ROOT_DIR+"\\"+sys.argv[3])

curfewAirport = df.loc[df['Station'] == sys.argv[2]]
print curfewAirport

curfewFromTime = curfewAirport['From Time']
curfewToPoint = curfewAirport['Final Time']

curfewToPointTime = curfewToPoint.to_string(index=False)
curfewFromPointTime = curfewFromTime.to_string(index=False)

curfewFromPointTime = pd.to_datetime(str(curfewFromPointTime)).time()
curfewToPointTime = pd.to_datetime(str(curfewToPointTime)).time()

print curfewFromPointTime
print curfewToPointTime

''' Read the output file and run a for loop which matches the airport with the curfew rule
Compare the range between the curfew time for a particular airport and the departure schedule
should be greater than 0'''
df = pd.read_csv(ROOT_DIR+"\\"+"output\\curfew_flight_schedule.csv")

for i in range(1, len(df)):
    arrivalTime = df.loc[i-1]['arrDateTimeNew']

    arrivalTimeNew = pd.to_datetime(str(arrivalTime)).time()
    print arrivalTimeNew

    if arrivalTimeNew >= curfewToPointTime or arrivalTimeNew <= curfewFromPointTime:
        assert True
    else:
        assert False
