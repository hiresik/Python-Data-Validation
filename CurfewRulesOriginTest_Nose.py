import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime, date, time, timedelta
import time
import string
import unittest
import nose
from delayed_assert import expect, assert_expectations
from ddt import ddt, data, file_data, unpack
from nose.tools import *

try:
    import yaml
except ImportError: # pragma: no cover
    have_yaml_support = False
else:
    have_yaml_support = True
    del yaml
# A good-looking decorator
needs_yaml = unittest.skipUnless(
have_yaml_support, "Need YAML to run this test"
)

@ddt
class Test:

    def setup(self):
        import yaml
        ''' Read the input file for MGT Rule '''
        self.rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Fetching data from Yml file
        stream = open(self.rootdir + "\\" + "data\\CurfewRules.yaml", "r")
        docs = yaml.load_all(stream)
        #
        for doc in docs:
             self.solver_output = doc['SolverOutput']
             self.curfew_rules = doc['CurfewRules']

        ''' Read the output file from Solver'''
        df = pd.read_csv(self.rootdir + "\\" + self.solver_output)



    @with_setup(setup)
    @needs_yaml
    @file_data(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\data\\origAirportID.yaml")
    def test(self, values):
        print values

        # ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        ''' Read the output file from Solver'''
        df = pd.read_csv(self.rootdir + "\\" + self.solver_output)

        '''Filter the Solver output on the basis of Destination Airport'''

        airPortValue = df.loc[df['origAirportID'] == values]

        airPortValue.to_csv("output/Vanilla_output_" + values + ".csv")

        # airPortValue = df.loc[df['origAirportID'] == sys.argv[2]]

        ''' Sort the output by flightNumber and store the result in output flight schedule file'''
        sortedValue = airPortValue.sort_values(by=['operationDate'])

        # sortedValue.to_csv(self.rootdir +'output/curfew_flight_schedule_origin.csv')

        ''' Read the Curfew rules and map it to the particular Airport
         and find the curfew time for a particular airport'''
        df = pd.read_csv(self.rootdir +"\\"+self.curfew_rules)

        curfewAirport = df.loc[df['Station'] == airPortValue]

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
        df = pd.read_csv(self.rootdir +"\\"+"output\\curfew_flight_schedule.csv")

        for i in range(1, len(df)):
            departureTime = df.loc[i-1]['dptDateTimeNew']

            departureTimeNew = pd.to_datetime(str(departureTime)).time()
            print departureTimeNew
            if departureTimeNew >= curfewToPointTime or departureTimeNew <= curfewFromPointTime:
                assert True
            else:
                assert False


#Nose tests
if __name__ == '__main__':
    nose.run(defaultTest=__name__)