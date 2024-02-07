# markdown-appender
import os

directory = r'' # replace this with the path to your designated folder

for filename in os.listdir(directory):
    if filename.endswith('.md'): # only consider markdown files
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith('tags::') and '#Quellen/Artikel' not in line:
                    lines[i] = line.strip() + ' #Quellen/Artikel\n'
                    file.seek(0)
                    file.writelines(lines)
                    break