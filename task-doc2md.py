import os

os.chdir('/home/anu/docfiles')
path = os.getcwd()
for root, dirs, files in os.walk('/home/anu/docfiles'):
    for file in files:
        if file.endswith('.doc'):
            os.chdir('/home/anu/docfiles')
            file_read = open(file, 'r',encoding='utf-8-sig')
            reader = file_read.readlines()
            os.chdir('/home/anu/docfiles')
            for lines in reader:
                print(lines)
                if lines.startswith('Book'):
                    book = lines[-4:-1]
                    try:
                        os.mkdir(book)
                    except:
                        os.chdir(path)
                elif lines.startswith('Chapter'):
                    chapter = lines[-3:-1]
                    os.chdir(path + '/' + book + '/')
                    try:
                        os.mkdir(chapter)
                    except:
                        os.chdir(path)
                else:
                    os.chdir(path + '/' + book + '/' + chapter + '/')
                    if lines.startswith('Verse'):
                        verse = lines[-3:-1]
                        writer = open(verse + '.md', 'w')
                    else:
                        writer.write(lines)
                os.chdir(path)
file_read.close()
writer.close()
