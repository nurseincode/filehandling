# open a file for writing - destructive - overwrites existing content
file = open('new_file.txt', 'w')

file.write('This is a new file!!\n')
file.write('Bye!\n')
file.close()

# file = open('new_file.txt', 'a') # append - keeps existing content & appends
