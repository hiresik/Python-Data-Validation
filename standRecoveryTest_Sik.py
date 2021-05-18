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
        ''' Read the input file for Stand Recover Rule '''
        self.rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Fetching data from Yml file
        stream = open(self.rootdir + "\\" + "data\\standRecoveryFiles.yaml", "r")
        docs = yaml.load_all(stream)

        for doc in docs:
            self.solver_output = doc['SolverOutput']
            self.stand_compatibility = doc['StandCompatibleRules']

        ''' Read the output file from Solver'''
        df = pd.read_csv(self.rootdir + "\\" + self.solver_output)


        df['BestInsert'].replace('none', np.nan, inplace=True)
        df.BestInsert.fillna(df.NewBay_prev,inplace=True)
        df.to_csv(self.rootdir + "\\" + "output/solver_output_best_insert.csv")


    @with_setup(setup)
    @needs_yaml
    @file_data(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\data\\FlightInput.yaml")
    def test(self, values):
        print values
        ''' Read the flight values from solver output'''
        df = pd.read_csv(self.rootdir + "\\" + "output/solver_output_best_insert.csv")
        df1 = pd.read_csv(self.rootdir + "\\" + self.stand_compatibility)
        flight_value = df.loc[df['Flight.Number'] == values]



        aircraftType = flight_value['aircraft_type']
        print aircraftType
        isUSFlight = flight_value['IsUSFlight']
        print isUSFlight
        bestInsert = flight_value['BestInsert']
        print bestInsert
        for j in bestInsert:
            if df1['StandValue'].to_string == bestInsert:
                print df1['StandValue']


        flight_value.to_csv(self.rootdir + "\\" + "output/solver_output_best_insert_" + values + ".csv")


        ''' Read the stand compatible rules'''

        # print stval
        # if df1['StandValue'] == flight_value['BestInsert']:
        # print (df1.loc[df1['StandValue'] == bestInsert])

        # print StandVal
        # security = StandVal['Security']
        # security =
        # bestInsert = flight_value['BestInsert']
        # aircraftType = flight_value['aircraft_type']
        # print aircraftType
        # isUSFlight = flight_value['IsUSFlight']
        # print isUSFlight
        # bestInsert = flight_value['BestInsert']
        # print bestInsert


        # for j in range(0, len(flight_value)):
        #     if df.loc[j][df['StandValue']] == bestInsert:
        #         print "hello"

#Nose tests
if __name__ == '__main__':
    nose.run(defaultTest=__name__)