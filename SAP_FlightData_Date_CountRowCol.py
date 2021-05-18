
import csv
from datetime import datetime

with open('C:\Docs\Lab 4\Data\SAP\Oct 2017 - Copy.csv', 'r') as source:
    with open('C:\Docs\Lab 4\Data\SAP\Oct 2017_out.csv', 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        # reader = csv.DictReader(source)
        header = ['ACOWNER','FLTNUM','FLIGHTDATE','DEPSTN','ARRSTN','MVTTYPE','MVTDATETIME','MVTDATETIMEUTC','EFFECTIVEFROM','EFFECTIVETO']
        source.readline()
        # source.read()
        for row in reader:
            # print row
            ts = row[2]
            ts1 = row[6]
            ts2 = row[7]
            ts3 = row[8]
            ts4 = row[9]
            ts = datetime.strptime(ts, '%d-%b-%y').strftime("%Y-%m-%d")
            ts1 = datetime.strptime(ts1, '%d-%b-%y').strftime("%Y-%m-%d")
            ts2 = datetime.strptime(ts2, '%d-%b-%y').strftime("%Y-%m-%d")
            ts3 = datetime.strptime(ts3, '%d-%b-%y').strftime("%Y-%m-%d")
            ts4 = datetime.strptime(ts4, '%d-%b-%y').strftime("%Y-%m-%d")
                
            if ts != "" or ts1 != "" or ts2 !="" or ts3 !="" or ts4 !="" :
                row[2] = ts 
                row[6] = ts1
                row[7] = ts2 
                row[8] = ts3
                row[9] = ts4  
            writer.writerow(row)
            

            # ts = row[6]
           
            # # print row[6]
            # ts = datetime.strptime(ts, '%m/%d/%Y').strftime("%Y-%m-%d hh:mm:ss")
            # # ts1 = datetime.strptime(ts1, '%m/%d/%Y').strftime("%Y-%m-%d")
            # if ts != "" or ts1 != "":
            #     writer.writerow(row)
   

source.close()
result.close()

# with open('C:\Docs\Lab 4\Data\SAP\Oct 2017_out.csv', 'rb') as newfile:
#     header = ['ACOWNER','FLTNUM','FLIGHTDATE','DEPSTN','ARRSTN','MVTTYPE','MVTDATETIME','MVTDATETIMEUTC','EFFECTIVEFROM','EFFECTIVETO']
#     wr = csv.writer(newfile, delimiter=',', quoting = csv.QUOTE_MINIMAL)
# newfile.close()


# count = 0
# with open("C:\Docs\Lab 4\Data\GE\PAX\PAX_11_25_March_2018_FORMATTED.csv", 'rb') as count_file:
#     csv_reader = csv.reader(count_file)
#     for row in csv_reader:
#         count += 1

# print "Before Merge", count

# aftermerge = 0
# with open("C:\Docs\Lab 4\Data\GE\PAX\PAX_11_25_March_2018_FORMATTED with date.csv", 'rb') as count_file:
#     csv_reader = csv.reader(count_file)
#     for row in csv_reader:
#         aftermerge += 1

# print aftermerge