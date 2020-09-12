#1. Create a bank account class that has 2 attributes - owner and balance
# And 2 methods - deposit and withdraw
# Withdrawals may not exceed the available balance

class Account():

    def __init__(self,owner,balance=0):
        self.owner =owner
        self.balance = balance

    def __str__(self):
        return """Account Owner: {}
Account Balance: ${}""".format(self.owner,self.balance)

    def deposit(self,amount):
        #self.balance = 0
        self.balance = self.balance + amount
        print('Deposit of ${} accepted'.format(amount))
        print('Current Balance is ${}'.format(self.balance))

    def withdraw(self,amount):
         if self.balance < amount:
             print('Sorry! not enough funds to withdraw ${}'.format(amount))
             print('Available balance is ${}'.format(self.balance))
         else:
             self.balance = self.balance - amount
             print('Withdrawal of ${} processed'.format(amount))
             print('Available Balance is ${}'.format(self.balance))


#Instantiate the class
acct1 = Account('Dolly',100)
print('*********************************************')
#Print the object
print(acct1)
print('*********************************************')
#Show the account owner attribute
print(acct1.owner)
print('*********************************************')
#Show the account balance attribute
print(acct1.balance)
print('*********************************************')
#Make a series of deposits and withdrawals
acct1.deposit(50)   #Deposit Accepted
print('*********************************************')
acct1.withdraw(25)  #Withdrawal processed
print('*********************************************')
#Make a withdrawal that exceeds available balance
acct1.withdraw(500) #Funds Unavailable!
print('*********************************************')