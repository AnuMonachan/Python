# getting factorial

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


print(factorial(4))

#List Comprehension

mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]
print(list(zip(mylist1, mylist2)))
print(set(zip(mylist1, mylist2)))
print(tuple(zip(mylist1, mylist2)))
print(dict(zip(mylist1, mylist2)))

li = tuple(x for x in "wordt")
print(li)
li = set(x for x in "wordt")
print(li)
li = list(x for x in "wordt")
print(li)

# list comprehension
celsius = [0, 7, 34, 36.4, 2]

fahrenheit = list((9 / 5 * temp + 32) for temp in celsius)
print(fahrenheit)

fahrenheit = list()

for temp in celsius:
    fahrenheit.append((9 / 5 * temp + 32))
print(fahrenheit)

lis = []

for x in (2, 4, 6):
    for y in (100, 200, 300):
        lis.append(x * y)
print(lis)

# if else in list comprehension
mylist3 = [z if z % 2 == 0 else "Odd" for z in range(0, 20)]
print(mylist3)

# nested for loop list comprehension

mylist = [x * y for x in (1, 2, 3) for y in (100, 200, 300)]
print(mylist)


# function

def say_hi(name):
    return ("Hello " + name + "!")


print(say_hi("Anu Monachan"))


# pig latin using function

def pig_latin(word):
    first_letter = word[0]
    if first_letter.lower() in "aeiou":
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"
    return pig_word


print(pig_latin(input("Enter word:")))


# working of *args

def myfunc(a, b, c=0, d=0, e=0):
    print(sum((a, b, c, d, e)))


myfunc(1, 2, 3, 2, 1)


# or this can be done by using args

def myfunc(*args):
    print(args)


myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9)

# armstrong

num = int(input())
order = len(str(num))
print(order)
sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print("armstrong")
else:
    print("not armstrong")
