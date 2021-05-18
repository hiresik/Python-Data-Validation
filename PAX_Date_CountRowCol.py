
import csv
from datetime import datetime

with open('C:\Docs\Lab 4\Data\GE\PAX\PAX.csv', 'r') as source:
    with open('C:\Docs\Lab 4\Data\GE\PAX\PAX_output.csv', 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        source.readline()
        for row in reader:
            ts = row[2]
            ts = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').strftime("%Y/%m/%d")
            if ts != "" or ts1 != "":
                row[2] = ts 
         
                writer.writerow(row)

source.close()
result.close()


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