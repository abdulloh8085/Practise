"""CLASS deep diving 
    (1) Encapsulation
    (2) Inheritence
    (3) Polymorphsm
"""

print("========= ENCAPSULATION ==========")
'''
C++, JAVA > public private protected
Encapsulation > public, __private__, _protected_
'''


class Account():
    # state
    description = "This class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit money")
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw money")
        self.__amount -= amount

    # getter va setter methodlar
    # decoraterlardan foidalanib

    @property
    def holder(self):
        return self.__owner

    @holder.setter  # tepa bilan bir hil bulishi kerak
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership: ", new_owner)
        self.__owner = new_owner


my_account = Account("Abdulloh", 4321)

my_account.deposit(231)
my_account.withdraw(1012)
my_account.get_balance()

print("-------------------")

my_account.owner = "Bob"  # no Change bcs it's private
my_account.get_balance()

try:
    result = my_account.amount
    print("result: ", result)
except Exception as err:
    print("No target state found", err)

print("-------------------")
account_owner = my_account.holder  # state (getter method)
print(account_owner)

my_account.holder = "Trump"
print(my_account.holder)
