f = open("3JN.usfm", "r", encoding='utf-8-sig')
a = f.read()
b = a.split("\n")
n = []
y = ('\\v', '\\h', '\\mt', '\\id','\\ide ','\\toc','\\s','\\c','\\b','\\p','\\f')
for x in b:
    if x.startswith(y):
        z = x.split(" ")
        w = z[0]
        n.append(w)
    else:
       pass
m = set(n)
for tag in m:
    print("valid tag = " + tag)