
import pandas as pd
from datetime import datetime
import time


df = pd.read_csv('C:\Docs\Lab 4\Data\SAP\Stand\StandEvolution.csv')



g = df.iloc[:,2].unique()

s = pd.Series(g).to_string(index=False)

ts = datetime.strptime(s,"%Y-%m-%d").date()

ts.to_csv('C:\Docs\Lab 4\Data\SAP\Stand\StandEvolution_output.csv') 
