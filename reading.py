    # Options to read a file
# file = open('new_file.txt')
# content = file.read() # Reads the entire content. For small files

# file = open('new_file.txt')

# content = file.readline().strip()
# print(content)
# content = file.readline() # One line at a time. Each call returns the next line
# print(content)
# content = file.readlines()
# print(content)

# content = file.read(10) # Reads 10 characters
# print(content)
# content = file.read(5) # Gets the next 5 characters
# print(content)

# for line in file: # for loop iterates over the lines in the file
   # print(line.strip())
# file.close()
# 'with' creates a context for the file
# When the block ends, the file will close automatically

with open('new_file.txt') as file:
    for line in file:
        print(line.strip())

