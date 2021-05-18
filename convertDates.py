import csv
from datetime import datetime

output_file = open(r"C:\Docs\Lab 4\Data\GE\Asset\ASSET_MASTER_2018_03_18_FORMATTED_01.csv", "wb")
fieldnames = ['AQUIRED_DATE', 'FIRST_IN_SERVICE_DATE']
writer = csv.DictWriter(output_file, fieldnames = fieldnames)
writer.writeheader()

with open(r"C:\Docs\Lab 4\Data\GE\Asset\ASSET_MASTER_2018_03_18_FORMATTED.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        output_row = {}
        output_row['AQUIRED_DATE'] = datetime.strptime(row['AQUIRED_DATE'], '%d/%m/%y').strftime('%d-%m-%y')
        # output_row['AQI'] = row['AQI']
        # output_row['Raw Conc.'] = row['Raw Conc.']
        writer.writerow(output_row)

output_file.close()