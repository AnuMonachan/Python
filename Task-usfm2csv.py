import csv

file = open('01-GEN.usfm', 'r+')
reader = file.readlines()
file_write = open('GEN.csv', 'w')
writer = csv.writer(file_write, delimiter='\t')
output_list = []
for lines in reader:
    if lines.startswith('\id '):
        book = lines[0:].strip('\\id ').strip('\n')
    if lines.startswith('\\c'):
        chapter = lines.strip('\\c ').strip('\n')
    if lines.startswith('\\v'):
        verse_num = lines[0:5].strip('\\v ').strip('\n')
        text = lines[5:].strip('\\v ').strip('\n')
        output_list.append([book, chapter, verse_num, text])
for lists in output_list:
    writer.writerow(lists)

file.close()
file_write.close()