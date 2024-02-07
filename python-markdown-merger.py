# this script merges markdown files with the same date
import os

# insert your folder path here
folder_path = r''

# Get a list of all markdown files in the folder
markdown_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]

# Create a dictionary to store the merged content of each date
merged_content = {}

# Loop through each markdown file
for file_name in markdown_files:
    # Get the date from the file name
    date = file_name.split()[0]
    # Open the file and read its contents
    with open(os.path.join(folder_path, file_name), "r") as f:
        content = f.read()
    # Check if the date already exists in the merged_content dictionary
    if date in merged_content:
        # If it does, add the current file's content to the existing content
        merged_content[date] += "\n" + content
    else:
        # If it doesn't, create a new key-value pair in the dictionary
        merged_content[date] = content

# Loop through the merged_content dictionary and write each merged file
for date, content in merged_content.items():
    # Create the file name for the merged file
    merged_file_name = f"{date} Merged.md"
    # Open the merged file and write the content to it
    with open(os.path.join(folder_path, merged_file_name), "w") as f:
        f.write(content)