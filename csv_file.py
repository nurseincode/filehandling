# with open('euro_cup_matches.csv') as file: # Option 1 of processing csv files using 'with'
# # Read the headings 
#     headings = file.readline().strip()
#     columns = headings.split(',')
#     print(columns)

# Option 2 using import csv

import csv

with open('euro_cup_matches.csv') as file: 
    content = csv.DictReader(file)
    for row in content:
        print(row)