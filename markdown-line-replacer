# this script removes the line and in a specific line
import os

directory = '/path/to/directory'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            new_lines = []
            for line in lines:
                if 'template date::' in line:
                    new_line = line.replace('[[', '').replace(']]', '')
                else:
                    new_line = line
                new_lines.append(new_line)
            new_content = ''.join(new_lines)
            with open(filepath, 'w', encoding='utf-8') as new_file:
                new_file.write(new_content)