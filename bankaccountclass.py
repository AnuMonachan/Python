#To create bank account with attributes owner name & balance

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
#method to take deposit 
    def deposit(self,amount):
        na = amount + acc.balance
        acc.balance = na
        print("new balance:" + str(na))
#method to withdraw cash  
    def withdraw(self,cash):
        if cash > acc.balance:
            print("Funds unavailable")
        else:
            print("withdrawal accepted")
            print("new balance:" + str(acc.balance - cash))

#inputs for Account owner data

acc = Account((input("name:")),int((input("balance:"))))
print(acc.owner)
print(acc.balance)
acc.deposit(int(input("amount to be deposited:")))
acc.withdraw(int(input("amount to be withdrawn:")))




