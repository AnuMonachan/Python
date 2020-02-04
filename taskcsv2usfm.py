import csv

file_read = open("GEN.csv", 'r')
csv_reader = csv.reader(file_read, delimiter='\t')
book_name = []
chapter_nums = []
for lines in csv_reader:  # lines[1] contains all chapter numbers & lines[0] contains book name
    chapter_nums.append(lines[1])
    book_name.append(lines[0])
book = book_name[0]
usfm_writer = open(book + '.usfm', 'w')
usfm_writer.write('\id ' + book + '\n')  # writes the book name to file
last_chapter_num = chapter_nums[-1]
first_chapter_num = chapter_nums[0]
chapter_num = int(first_chapter_num)  # b holds the first chapter no.
set_of_chapters = sorted(set(row for row in chapter_nums))
chapter = []  # chapter holds all the chapter no.s in the book
t = 0
for chapters in set_of_chapters:
    chapter.append(chapters)


def write():
    if t < len(chapter):
        usfm_writer.write("\c " + str(chapter_num) + "\n")  # this writes all the chapters of book available in the csv file
    file_read.seek(0)
    for line in csv_reader:
        if line[1] == str(chapter_num):
            usfm_writer.write('\\v ' + line[2] + ' ' + line[3] + '\n')  # writes the verse no.s and techapter_numt


n = 1
while n <= int(last_chapter_num):
    write()
    chapter_num = chapter_num + 1
    n = n + 1
    t = t + 1

file_read.close()
usfm_writer.close()