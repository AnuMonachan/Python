import glob
import os
import pandas as pd
os.chdir('/home/anu/Downloads/')
list_files = sorted(glob.glob('/home/anu/Downloads/1JN/**/*.md'))
txt = []
book = []
verse = []
chapter = []
# list files contains all files with .md and their path

for files in list_files:
    file = open(files, 'r')
    reader = file.readlines()
    book.append(files[-12:-9])
    verse.append(files[-5:-3])
    chapter.append(files[-8:-6])
    for line in reader:
        content = ''.join(reader).replace('#','•')
    txt.append(content)
data = {'Book': book,
        'Notes': txt,
        'Verses': verse,
        'Chapter': chapter}
df = pd.DataFrame(data, columns=['Book', 'Chapter', 'Verses', 'Notes'])
df.to_excel(book[1]+'.xlsx', index=None)
file.close()
