    
import csv

# r='C:\Docs\Lab 4\Data\stemp_for_date.csv'
# w='C:\Docs\Lab 4\Data\stemp_for_date_out.csv'


r='C:\Docs\Lab 4\Data\SAP\ULD scanning\ULD Scanning Formatted\ULD Scanning_001_Aug17_DEC17_JAN18_FEB18_Masked.csv'
w='C:\Docs\Lab 4\Data\stemp_for_date_out.csv'


with open(r, 'r') as source:
    with open(w, 'w') as result:
        writer = csv.writer(result, lineterminator='\n')
        reader = csv.reader(source)
        data = [line for line in reader]
        # headers = reader.fieldnames()
        writer.writerow(["PAX_ID","FLIGHT_NUMBER","OPERATION_DATE_GMT","REC_LOCATOR","ORIGIN","DESTINATION","CABIN_CLASS"])
        writer.writerows(data)




result.close()
source.close()

count = 0
with open(r, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1

print "Source Count ", count

aftermerge = 0
with open(w, 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        aftermerge += 1

print "Output count ",aftermerge