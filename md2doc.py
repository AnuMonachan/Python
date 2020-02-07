import glob
import os

path = '/home/anu/Downloads/1JN/'

os.chdir('/home/anu/Downloads/')
list_files = sorted(glob.glob('/home/anu/Downloads/1JN/**/*.md'))
for files in list_files:
    file = open(files, 'r')
    reader = file.readlines()
    book_name = files[-12:-9]
    w = open(book_name + '.doc', 'w')
w.write('Book : ' + book_name + '\n')
for files in list_files:
    file = open(files, 'r')
    reader = file.readlines()
    verse_num = files[-5:-3]
    chapter_num = files[-8:-6]
    if verse_num == '01':
        if chapter_num == '01':
            w.write('Chapter : ' + chapter_num
                    + '\n')
            w.write('Verse : ' + verse_num + '\n'
                    + '\n')
        else:
            w.write('\n' +
                    '\n' +
                    'Chapter : ' + chapter_num
                    + '\n')
            w.write('Verse : ' + verse_num + '\n'
                    + '\n')
    else:
        w.write("\n"
                + '\n'
                + 'Verse : ' + verse_num + '\n'
                + '\n')
    for line in reader:
        print(line)
        w.write(' ' + line + ' ')

file.close()

w.close()