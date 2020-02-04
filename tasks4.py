# - Finding lines starting with vowel. - Task 4(1)

x = ('a', 'e', 'i', 'o', 'u')
with open('newfile.txt', 'r') as work:
    for sentence in work:
        if sentence.startswith(x):
            print(sentence)



# - Put Question mark after interrogative words. - Task 4(2)

x = ("How","Why","What","Who","Whom","Where","When","Which","Whose")

s = "How are You\n"\
    "Hi, i am learning Python\n" \
    "When are you coming"
a = s.split("\n")
for l in a:
    if l.startswith(x):
        print(l + "?")
    else:
        print(l + ".")

