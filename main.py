import os

folder_path = 'count-these'
total_lines = 0

# Function to count lines in a file
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except Exception as e:
        print(f"Error counting lines in {file_path}: {e}")
        return 0

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through each file and count lines
for file_name in files:
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_path = os.path.join(folder_path, file_name)
        line_count = count_lines(file_path)
        total_lines = total_lines + line_count
        print(f"File: {file_name}, Lines: {line_count}")

print(f"\nTotal: {total_lines}")