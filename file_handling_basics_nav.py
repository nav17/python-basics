import os

# pwd - print the current working directory
print("Current Working Directory: ", os.getcwd())


# File Paths

TEXT_FILE_NAME = "data.txt"  # all caps means constant value / doesn't change

file_path = os.getcwd() + '/' + TEXT_FILE_NAME

# doesn't work across OSs
# Better way:
file_path = os.path.join(os.getcwd() + '/' + TEXT_FILE_NAME)

# New way to do it with importing Path library

from pathlib import Path

current_dir = Path.cwd()

TEXT_FILE_NAME = 'data.txt'

file_path = current_dir / TEXT_FILE_NAME

print(file_path)

# Check if a file exists

if (Path.exists(file_path)):
    print("File exists!")
else:
    print("File not found!")
    
# Make a new directory

Path.mkdir("new_directory", )
