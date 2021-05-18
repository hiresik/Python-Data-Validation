import csv
import os

f1 = file('files\DataForValidation_VanillaSolution_3Mar.csv', 'r')
f2 = file('mask\Stand_Comaptibility.csv', 'r')
f3 = file('output\streoutput02.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

mask_files = list(c2)

for files_row in c1:
    row = 1
    found = False
    for mask_row in mask_files:
        results_row = files_row
        if files_row[20]+files_row[17] == mask_row[2]+mask_row[8]:
            results_row.append('FOUND in stand comp. list (row ' + str(row) + ')')
            found = True
            break
        row = row + 1
    if not found:
        results_row.append('NOT FOUND in stand comp. list')
    c3.writerow(results_row)
f1.close()
f2.close()
f3.close()


input = open('output\streoutput02.csv', 'rb')
output = open('output\streoutput02_1.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row:
        writer.writerow(row)
input.close()
output.close()


os.remove("output\streoutput02.csv")
os.rename('output\streoutput02_1.csv', 'output\streoutput02.csv')



