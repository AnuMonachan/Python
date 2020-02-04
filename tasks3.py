# Takes 2 inputs and generates 2-D array. - Task 3(1)

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
my_list = []

for row in range(rows):
    my_list.append([])
    for col in range(columns):
        my_list[row].append(0)

for row in range(rows):
    for col in range(columns):
        my_list[row][col]= row*col

print(my_list)


# Calculate the count of letters and digits in a sentence. - Task 3(2)

sentence: str = input("Sentence:")
letters = 0
digits = 0
for x in sentence:
    if x.isnumeric():
        digits = digits + 1
    elif x.isalpha():
        letters = letters + 1
    else:
        pass
print("No. of letters in sentence is " + str(letters))
print("No. of digits in sentence is " + str(digits))


