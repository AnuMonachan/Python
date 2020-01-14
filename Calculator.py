#function to initiate calculation

def calculate():
    print('''
    use: ~ for square root
         ^ for square
         + for addition
         - for subtraction
         * for multiplication
         / for division
         % for modulus
         
    ''')
#inputs by user
    n1=float(input("n1:"))
    op=input("op:")
    if op == "~":
        print(n1**0.5)
    elif op == "^":
        print(n1**2)
    else:
        n2=float(input("n2:"))


        if op=="+":
            print(n1+n2)
        elif op=="-":
            print(n1-n2)
        elif op=="*":
            print(n1*n2)
        elif op=="/":
            print(n1/n2)
        elif op=="%":
            print(n1%n2)
        elif op=="_":
            print((n1+n2)/2)
        else:
            print("invalid")

calculate()

#allow repeated calculations

print('''
Do u want to continue?
If Yes press 'Y'
If No press 'N'
''')
while input("Continue:").upper() == "Y":
    calculate()
else:
    print("End")






