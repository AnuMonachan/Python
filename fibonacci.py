#fibonacci using while loop
n = int(input('n:'))
x = 0
a = 0
b = 1

#function for fibonacci series of 'n' values:

while x < n:
    if x <= 1:
        c = x
    else:
        c = a + b
        a, b = b, c
    print(c)
    x = x + 1

#fibonacci using for loop

a=0
b=1

#function for fibonacci series of 'n' values:

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for x in range(2,n):
        c = a+b
        a,b = b,c
        print(c)

fib(int(input()))