# basic encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"deposited Rs.{amt}. balance: Rs.{self.balance}")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"withdrew Rs.{amt}. balance: Rs.{self.balance}")
        else:
            print("insufficient balance!")

acc = BankAccount("Jay", 5000)
acc.deposit(2000)
acc.withdraw(3000)
acc.withdraw(9000)


# public - no prefix
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Jay")
print(s.name)
s.name = "Rahul"
print(s.name)


# protected - single underscore (convention only)
class Student:
    def __init__(self, name, roll):
        self.name = name
        self._roll = roll

s = Student("Jay", 101)
print(s._roll)


# private - double underscore (name mangling)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

acc = BankAccount(1000)

try:
    print(acc.__balance)
except AttributeError as e:
    print(f"error: {e}")

print(acc._BankAccount__balance)


# access modifiers together
class Employee:
    def __init__(self):
        self.name = "Jay"
        self._dept = "IT"
        self.__salary = 50000

e = Employee()
print(e.name)
print(e._dept)
# print(e.__salary)  # error


# getter and setter
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, bal):
        if bal >= 0:
            self.__balance = bal
            print(f"balance updated to Rs.{self.__balance}")
        else:
            print("invalid! can't be negative")

acc = BankAccount(1000)
print(f"balance: Rs.{acc.get_balance()}")

acc.set_balance(2000)
acc.set_balance(-500)
print(f"final: Rs.{acc.get_balance()}")


# @property - pythonic getter/setter
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, val):
        if val >= 0:
            self.__balance = val
        else:
            print("invalid! can't be negative")

    @balance.deleter
    def balance(self):
        print("can't delete balance!")

acc = BankAccount("Jay", 1000)
print(f"balance: Rs.{acc.balance}")

acc.balance = 5000
print(f"balance: Rs.{acc.balance}")

acc.balance = -100
print(f"balance: Rs.{acc.balance}")

del acc.balance


# practical example
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self._age = age
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, val):
        if val in ["A", "B", "C", "D", "F"]:
            self.__grade = val
        else:
            print(f"invalid grade: {val}")

    def display(self):
        print(f"{self.name}, age: {self._age}, grade: {self.__grade}")

s = Student("Jay", 21, "A")
s.display()

s.grade = "B"
s.display()

s.grade = "Z"
s.display()
