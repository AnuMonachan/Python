f = open('filecheck.txt','r')

f1 = open('created.txt','a')
f1.write('nothing\n')
f1.write('something\n')

for data in f:
    f1.write(data)