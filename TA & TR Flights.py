

import pandas as pd
import pandasql as pds
import numpy as np
np.set_printoptions(threshold=np.nan)

r='C:\Docs\Lab 4\Data\SAP\Stand\StandEvolution.csv'
w='C:\Docs\Lab 4\Data\tr_vanilla_solution.csv'




df=pd.read_csv(w)
# df = pd.read_csv('C:\Docs\Lab 4\Data\SAP\FlightMovementType\Oct 2017.csv', header=None, usecols=[2])
# print df['DEP_DATE'].unique()

# q1 = """select distinct Date from df"""
# print "starting sql....."
# print pds.sqldf(q1, locals())
# print "ending sql....."

print df['aircraftID'].unique()

print df.groupby(['aircraftID']).count()