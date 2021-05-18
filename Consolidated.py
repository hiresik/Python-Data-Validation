import pandas as pd
import datetime
count = 0
for chunk in pd.read_csv("masked_2_crew_activities_all.csv", chunksize=1000000):
   data = chunk
   ranks = ['PUR', 'CSV', 'FG1', 'GR1', 'GR2', 'CSA','SFS','CA','FO','GI']

   for row in data['masked_2_crew_activities_all.qualifiedrank']:
       if row not in ranks:
           count += 1
   

           # print(row)
print('Number of records are not having valid rank = ',count )

print('******************************')

for chunk in pd.read_csv("masked_2_crew_activities_all.csv", chunksize=10000):
    data = chunk
    expectedColumns = ['masked_2_crew_activities_all.staffno', 'masked_2_crew_activities_all.reasoncode', 'masked_2_crew_activities_all.reasontext', 'masked_2_crew_activities_all.qualifiedrank', 'masked_2_crew_activities_all.activitycode', 'masked_2_crew_activities_all.activitybegtime', 'masked_2_crew_activities_all.activityendtime', 'masked_2_crew_activities_all.effectivefrom', 'masked_2_crew_activities_all.effectiveto']
    assert (list(data.columns.get_values())== expectedColumns),'Columnnames are not matching'
print('Expected and actual Culumn names and numbers are matching')

print('******************************')
count=0
for chunk in pd.read_csv("masked_2_crew_activities_all.csv", low_memory=False, chunksize=100000):
    data = chunk

    for row in data['masked_2_crew_activities_all.activitybegtime']:
        try:
            # print(row)
            date = datetime.datetime.strptime(row, "%Y-%m-%d %H:%M:%S.0")
            #date = datetime.datetime.strptime(row, "%d/%m/%Y %H:%M")
        except:
            count += 1

print('Number of activitybegtime are not following the expected date time format',count)

print('******************************')

count=0
for chunk in pd.read_csv("masked_2_crew_activities_all.csv", low_memory=False, chunksize=100000):
    data = chunk

    for row in data['masked_2_crew_activities_all.effectivefrom']:
        try:
            # print(row)
            date = datetime.datetime.strptime(row, "%Y-%m-%d %H:%M:%S.0")
            #date = datetime.datetime.strptime(row, "%d/%m/%Y %H:%M")
        except:
            count += 1

print('Number of effectivefrom are not following the expected date time format',count)

print('******************************')

count=0
for chunk in pd.read_csv("masked_2_crew_activities_all.csv", low_memory=False, chunksize=100000):
    data = chunk

    for row in data['masked_2_crew_activities_all.effectiveto']:
        try:
            # print(row)
            date = datetime.datetime.strptime(row, "%Y-%m-%d %H:%M:%S.0")
            #date = datetime.datetime.strptime(row, "%d/%m/%Y %H:%M")
        except:
            count += 1

print('Number of effectiveto are not following the expected date time format',count)

print('******************************')

count=0
for chunk in pd.read_csv("masked_2_crew_activities_all.csv", low_memory=False, chunksize=100000):
    data = chunk

    for row in data['masked_2_crew_activities_all.activitybegtime']:
        try:
            # print(row)
            date = datetime.datetime.strptime(row, "%Y-%m-%d %H:%M:%S.0")
            #date = datetime.datetime.strptime(row, "%d/%m/%Y %H:%M")
        except:
            count += 1

print('Number of activitybegtime are not following the expected date time format',count)

print('******************************')