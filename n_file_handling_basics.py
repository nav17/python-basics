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

TEXT_FILE_NAME = 'demo_files/data.txt'

file_path = current_dir / TEXT_FILE_NAME

print(file_path)

# Check if a file exists

if (Path.exists(file_path)):
    print("File exists!")
else:
    print("File not found!")
    
# Make a new directory

new_directory_path = current_dir / "new_directory"
new_directory_path.mkdir(exist_ok=True)
# exist_ok stops recreating if already exists

# Opening a file
opened_file = open(file_path)
print(opened_file)  # prints file info

with open(file_path) as file:
    # can do stuff with file contents
    print(file.read())
  
# context manager (the with block) automatically closes the file
# when block is exited, no more reads allowed