# find all numbers which should divisible by 7 but are not a multiple of 5, between 900 and 2000 - Task 2(1)

x = list(range(900, 2000))

for num in x:
    if num % 7 == 0 and num % 5 != 0:
        print(num)

print("\n")

# Task 2(2)

print('Accepts comma-separated words as input and prints the words in a comma separated sequence after sorting them '
      'alphabetically.\n')

my_words = "without,hello,bag,world"
words = my_words.split(",")
words.sort()
print(','.join(words))
print("\n")


# accept statement and capitalize - Task 2(3)

text = ('hello world\n'
        'practice makes Perfect')
z = text.split("\n")
for word in z:
    print(word.capitalize())
y = text.title()
print(y)

# Task 2(4)

print('Accepts a sequence of whitespace-separated words, and show after removing duplicates and sort them as well.\n')

my_sentence = "hello world and practice makes perfect and hello world again"
split_sentence = my_sentence.split(' ')
new_sentence = []

for word in split_sentence:
    if word not in new_sentence:
        new_sentence.append(word)
    else:
        continue
new_sentence.sort()
print(' '.join(new_sentence))

