import pandas as pd
import pprint
from datetime import datetime, date, time, timedelta
from dateutil.parser import parse

df = pd.read_csv('C:\\Users\\S731377\\Documents\\LAB4\\SAP\\StandEvolution\\000000_0.csv')



g = df.iloc[:, 2].unique()

s = pd.Series(g).to_string(index=False)

ts = datetime.strptime(s, "%Y-%m-%d").date()
print "ts value"
ts.to_csv("C:\\testAutomation\\Hermes\\Lab4\\output\\output.csv")