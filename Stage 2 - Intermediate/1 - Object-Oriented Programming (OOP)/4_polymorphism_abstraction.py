from abc import ABC, abstractmethod

# polymorphism - same method, different behavior
class Dog:
    def sound(self):
        print("bark")

class Cat:
    def sound(self):
        print("meow")

class Cow:
    def sound(self):
        print("moo")

animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.sound()


# method overriding
class Animal:
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self):
        print("bark!")

class Cat(Animal):
    def sound(self):
        print("meow!")

Dog().sound()
Cat().sound()


# calling parent method from override
class Animal:
    def sound(self):
        print("animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("...specifically, a bark!")

Dog().sound()


# polymorphism with built-in functions
print(len("Python"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))


# duck typing
class Dog:
    def speak(self):
        print("bark")

class Person:
    def speak(self):
        print("hello")

class Robot:
    def speak(self):
        print("beep boop")

def make_speak(obj):
    obj.speak()

make_speak(Dog())
make_speak(Person())
make_speak(Robot())


# abstraction using abc
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def breathe(self):
        print("breathing...")

class Dog(Animal):
    def sound(self):
        print("bark")

    def move(self):
        print("running on four legs")

class Bird(Animal):
    def sound(self):
        print("tweet")

    def move(self):
        print("flying")

try:
    a = Animal()
except TypeError as e:
    print(f"error: {e}")

d = Dog()
b = Bird()

d.sound()
d.move()
d.breathe()

b.sound()
b.move()


# mixins
class LogMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")

class SerializableMixin:
    def serialize(self):
        return str(self.__dict__)

class User(LogMixin):
    def __init__(self, name):
        self.name = name

class Admin(User, SerializableMixin):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

admin = Admin("Jay", "Super")
admin.log("admin created")
print(admin.serialize())


# mixin reuse
class LogMixin:
    def log(self, msg):
        print(f"[LOG] {self.__class__.__name__}: {msg}")

class User(LogMixin):
    def __init__(self, name):
        self.name = name

class Order(LogMixin):
    def __init__(self, order_id):
        self.order_id = order_id

class Payment(LogMixin):
    def __init__(self, amt):
        self.amt = amt

User("Jay").log("user created")
Order("ORD-001").log("order placed")
Payment(5000).log("payment done")


# payment system (inheritance + polymorphism + abstraction)
class Payment(ABC):
    @abstractmethod
    def pay(self, amt):
        pass

    @abstractmethod
    def refund(self, amt):
        pass

class UpiPayment(Payment):
    def pay(self, amt):
        print(f"paid Rs.{amt} via UPI")
    def refund(self, amt):
        print(f"refunded Rs.{amt} via UPI")

class CardPayment(Payment):
    def pay(self, amt):
        print(f"paid Rs.{amt} via card")
    def refund(self, amt):
        print(f"refunded Rs.{amt} to card")

class CashPayment(Payment):
    def pay(self, amt):
        print(f"paid Rs.{amt} in cash")
    def refund(self, amt):
        print(f"refunded Rs.{amt} in cash")

payments = [UpiPayment(), CardPayment(), CashPayment()]
for p in payments:
    p.pay(1000)


# overriding vs overloading
class Animal:
    def sound(self):
        print("generic sound")

class Dog(Animal):
    def sound(self):
        print("bark")

Dog().sound()

# python doesn't have overloading, use default args
def add(a, b=0, c=0):
    return a + b + c

print(add(5))
print(add(5, 10))
print(add(5, 10, 20))
