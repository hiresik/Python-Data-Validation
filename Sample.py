import pandas as pd
import pprint
from datetime import datetime, date, time, timedelta
from dateutil.parser import parse

#colnames=['Airline', 'Flight Number',    'FlightDate',  'Arr-Dep Flag', 'Old Bay',  'New Bay',  'Current Gate', 'ChangeDate']

colnames=['department', 'workarea','task_type', 'task_remark', 'task_orientation', 'task_state','inb_flight', 'inb_aircraft','sta',
          'eta','ata','inb_reg','inb_rou','inb_flight_status','inb_flight_type','inb_pos','inb_gate','inb_bkd_load','out_flight',
          'out_aircraft','std','etd','atd','out_reg','out_rou','out_flight_status','out_flight_type','out_pos','out_gate',
          'out_bkd_load','staff','staff_id','shift_pln_start_time','shift_pln_end_time','shift_act_start_time','shift_act_end_time',
          'task_date','shift_function','task_requirement','equipment','task_rule_name','task_no','order_start_time','order_end_time',
          'task_duration','task_setup__duration1','task_setup__duration2','task_clearup__duration1','task_clearup__duration2','planned_start',
          'planned_end','planned__duration','start_loc','end_loc']

#df = pd.read_csv('C:\\Users\\S731377\\Documents\\LAB4\\SAP\\StandEvolution\\000000_0.csv', names=colnames, header=None)
df = pd.read_csv('C:\\Users\\S731377\\Documents\\LAB4\\SAP\\RTC_Cleaning\\000000_0.csv', names=colnames, header=None)
#df = pd.read_csv('C:\\Users\\S731377\\Documents\\LAB4\\SAP\\RTC_Cleaning\\000000_0.csv', names=colnames, header=None)
#print df
df.to_csv('C:\\Users\\S731377\\Documents\\LAB4\\SAP\\RTC_Cleaning\\output.csv');
# ts = df['FlightDate'].to_string(index=False)
# ts = datetime.strptime(ts, '%Y-%m-%d %H:%M')
#data = df['\N'].str[:10]
data = df['task_date']
data = data.drop_duplicates()
data.to_csv("C:\\Users\\S731377\\Documents\\LAB4\\SAP\\RTC_Cleaning\\outputdate.csv")

#date_value = df['Date'].to_string(index=False)
#print date_value
# try:
#     print df.ix[df[date_value]]
#     datetime.strptime(date_value, '%Y-%m-%d %H:%M')
# except ValueError:
#     #print df[date_value]
#     print df.ix[df[date_value]]
#     raise ValueError("Incorrect data format, should be YYYY-MM-DD")
#
#print data


#print pd.to_datetime(df['FlightDate'].str.strip(), dayfirst=True)
#cr_date = datetime.strptime(data, "%Y-%m-%d")
#cr_date = pd.to_datetime(data)
#print cr_date
# print df['FlightDate']
#print pd.DatetimeIndex(df.FlightDate).normalize()
#print ts.dt.normalize()
#print df['FlightDate']

#print pd.DatetimeIndex(df.FlightDate).normalize()

#
# g = df.iloc[:, 2].unique()
#
# s = pd.Series(g).to_string(index=False)
#
# ts = datetime.strptime(s, "%Y-%m-%d").date()
#
# ts.to_csv("C:\\testAutomation\\Hermes\\Lab4\\output\\output.csv")