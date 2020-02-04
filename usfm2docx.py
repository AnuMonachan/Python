f = open('1JN.usfm','r')
r = f.readlines()
o = open('1JN.docx','w')
for lines in r:
    if lines.startswith('\\id'):
        o.write(lines[4:])
    if lines.startswith('\\c'):
        o.write('अध्याय' + lines[3:] )
    if lines.startswith('\\v'):
        o.write(lines[3:])

o.close()
f.close()
