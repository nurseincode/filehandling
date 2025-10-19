# JSON - Javascript Object Notation 
import json

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

with open('matches.json', 'w') as file:
    json.dump(matches, file, indent=4)