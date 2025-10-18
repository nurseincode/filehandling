# with open('euro_cup_matches.csv') as file: # Option 1 of processing csv files using 'with'
# # Read the headings 
#     headings = file.readline().strip()
#     columns = headings.split(',')
#     print(columns)

# Option 2 using import csv

import csv

# with open('euro_cup_matches.csv') as file: 
#     content = csv.DictReader(file)
#     for row in content:
#         print(row)

total_goals = 0
with open('euro_cup_matches.csv') as file: 
    content = csv.DictReader(file) # Dictreader reads the headers from the file
    for row in content:
        total_goals += int(row['Score A']) + int(row['Score B'])
print(f'Total goals in tournament so far: {total_goals}')

# Writing CSV files
# with open('new_matches.csv', 'w') as file: # Reusing file 
#     writer = csv.DictWriter(file, ['Team A', 'Team B', 'Score A', 'Score B', 'Date']) # Defining column headers(field names) explicitly
#     writer.writeheader() # Writes the first row using above fieldnames as col headers
#     writer.writerow({
#         'Team A': 'Portugal',
#         'Team B': 'Spain',
#         'Score A': 1,
#         'Score B': 1,
#         'Date': '2024-04-15'
#     })

# Using writerrows to call dicts in a list

matches = [ 
    {
        'Team A': 'Spain',
        'Team B': 'Italy',
        'Score A': 1,
        'Score B': 1,
        'Date': '2024-04-20'
    },
    {
        'Team A': 'France',
        'Team B': 'Germany',
        'Score A': 1,
        'Score B': 1,
        'Date': '2024-04-15'
    }
]
with open('new_matches.csv', 'w') as file: 
    # writer = csv.DictWriter(file, ['Team A', 'Team B', 'Score A', 'Score B', 'Date']) 
    writer = csv.DictWriter(file, matches[0].keys()) # No redundancy 
    writer.writeheader() 
    writer.writerows(matches) # Calling the matches from the list
      
