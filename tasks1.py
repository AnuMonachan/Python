# finding word with length less than 4 - Task 1(1)

x = "Transpose your CSV file By doing this your rows convert to column and vice versa."

y = x.split()

for word in y:
    if len(word) < 4:
        print(word)


# add new word on first position in array - Task 1(2)

b = ['test', 'ok', 'how', 'why', 'hello']

b.insert(0, input("Word You Want To Add:"))

print(b)

# add new word on last position in array - Task 1 (3)

a = ['whereas', 'ok', 'how', 'elephant', 'hello']

a.append(input("Word You Want To Add:"))

print(a)

# find and remove word from array and add to new array - Task 1 (4)

c = ['whereas', 'ok', 'how', 'elephant', 'hello']
d = []
for word in c:

    if len(word) < 4:
        print(word)
        d.append(word)
        print(d)
for word in d:
    c.remove(word)
print(c)

# create csv file - Task 1(5)

import csv

with open('task_csv.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name"])
    writer.writerow(["Anu"])
