# single inheritance
class Animal:
    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")

class Dog(Animal):
    def bark(self):
        print("barking")

d = Dog()
d.eat()
d.sleep()
d.bark()


# multilevel inheritance
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")

class Puppy(Dog):
    def play(self):
        print("playing")

p = Puppy()
p.eat()
p.bark()
p.play()


# hierarchical inheritance
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")

class Cat(Animal):
    def meow(self):
        print("meowing")

d = Dog()
c = Cat()

d.eat()
d.bark()
c.eat()
c.meow()


# multiple inheritance
class Father:
    def skills(self):
        print("programming")

class Mother:
    def hobbies(self):
        print("painting")

class Child(Father, Mother):
    pass

ch = Child()
ch.skills()
ch.hobbies()


# same method in both parents
class A:
    def show(self):
        print("A's show")

class B:
    def show(self):
        print("B's show")

class C(A, B):
    pass

obj = C()
obj.show()


# MRO - method resolution order
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

print(C.mro())


# super()
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Tommy", "Labrador")
print(d.name, d.breed)


# super() in 3-level hierarchy
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Puppy(Dog):
    def __init__(self, name, breed, toy):
        super().__init__(name, breed)
        self.toy = toy

p = Puppy("Max", "Beagle", "Ball")
print(p.name, p.breed, p.toy)


# IS-A (inheritance) vs HAS-A (composition)
class Animal:
    def breathe(self):
        print("breathing")

class Dog(Animal):
    pass

class Engine:
    def start(self):
        print("engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("car ready")

car = Car()
car.start()


# practical example
class Employee:
    company = "ScaleTech"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} | Rs.{self.salary} | {self.company}")

class Developer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.lang = lang

    def code(self):
        print(f"{self.name} is coding in {self.lang}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage(self):
        print(f"{self.name} is managing {self.team_size} people")

dev = Developer("Jay", 50000, "Python")
mgr = Manager("Rahul", 80000, 10)

dev.display()
dev.code()

mgr.display()
mgr.manage()
