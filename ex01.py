"""
Make a class that represents a bank account. Create four methods
named set_details, display, withdraw and deposit.

In the set_details method, create two instance variables : name and balance.
The default value for balance should be zero. In the display method,
display the values of these two instance variables.

Both the methods withdraw and deposit have amount as parameter.
Inside withdraw, subtract the amount from balance and inside deposit,
add the amount to the balance.

Create two instances of this class and call the methods on those instances.
"""

class Account:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

acc1 = Account()
acc1.set_details("Tom")
acc1.display()
acc1.deposit(100)
acc1.display()
acc1.withdraw(50)
acc1.display()
print()

acc2 = Account()
acc2.set_details("Kim", 100)
acc2.display()
acc2.deposit(100)
acc2.display()
acc2.withdraw(50)
acc2.display()


