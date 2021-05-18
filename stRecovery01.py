import csv

with open('mask\Stand_Comaptibility.csv', 'rb') as master:
    maskit = dict((r[1], i) for i, r in enumerate(csv.reader(master)))

with open('files\DataForValidation_VanillaSolution_3Mar.csv', 'rb') as filesit:
    with open('output\streoutput01.csv', 'wb') as results:
        reader = csv.reader(filesit)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['RESULTS'])

        for row in reader:
            index = maskit.get(row[22])
            if index is not None:
                message = 'FOUND in master list (row {})'.format(index)
            else:
                message = 'NOT FOUND in master list'
                writer.writerow(row + [message])