import os

# Specify the directory path
directory_path = "C:/Users/Suraj/Documents"  # Change this to your desired path

# List all files and folders in the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You don't have permission to access this directory.")
