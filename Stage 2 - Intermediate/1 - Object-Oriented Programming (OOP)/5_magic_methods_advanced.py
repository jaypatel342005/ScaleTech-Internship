# __str__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"student: {self.name}, age: {self.age}"

s = Student("Jay", 21)
print(s)


# __repr__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"student: {self.name}"

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age})"

s = Student("Jay", 21)
print(str(s))
print(repr(s))


# __len__
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)+1

t = Team(["Jay", "Rahul", "Priya"])
print(len(t))


# __eq__
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

s1 = Student("Jay", 101)
s2 = Student("Rahul", 101)
s3 = Student("Priya", 102)

print(s1 == s2)
print(s1 == s3)


# __add__ (operator overloading)
class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Number(self.val + other.val)

    def __str__(self):
        return str(self.val)

a = Number(10)
b = Number(20)
c = a + b
print(f"{a} + {b} = {c}")


# operator overloading - full example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

print(f"p1 + p2 = {p1 + p2}")
print(f"p2 - p1 = {p2 - p1}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p2: {p1 < p2}")


# __getitem__
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

obj = MyList([10, 20, 30, 40, 50])
print(obj[0])
print(obj[2])
print(len(obj))


# __call__
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(f"{self.greeting}, {name}!")

greet = Greeter("Hello")
greet("Jay")
greet("Rahul")


# instance vs class vs static method
class Student:
    college = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name}, age: {self.age}, college: {Student.college}")

    @classmethod
    def change_college(cls, new):
        cls.college = new

    @staticmethod
    def is_adult(age):
        return age >= 18

s = Student("Jay", 21)
s.display()

Student.change_college("XYZ University")
s.display()

print(Student.is_adult(21))
print(Student.is_adult(15))


# escape characters
print("hello\nworld")
print("name:\tJay")
print("C:\\Users\\Jay")
print("he said \"hello\"")
print('it\'s python')
print("hello\rworld")
print("hello\b world")


# raw strings
print("C:\\Users\\Jay\\Documents")
print(r"C:\Users\Jay\Documents")


# complete example - employee management
class Employee:
    company = "ScaleTech"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, val):
        if val > 0:
            self.__salary = val

    def work(self):
        print(f"{self.name} is working")

    def __str__(self):
        return f"Employee: {self.name} | Rs.{self.__salary}"

    def __eq__(self, other):
        return self.name == other.name and self.__salary == other.__salary

class Developer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.lang = lang

    def work(self):
        print(f"{self.name} is developing in {self.lang}")

    def __str__(self):
        return f"Developer: {self.name} | {self.lang} | Rs.{self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing {self.team_size} people")

    def __str__(self):
        return f"Manager: {self.name} | team: {self.team_size} | Rs.{self.salary}"


dev1 = Developer("Jay", 50000, "Python")
dev2 = Developer("Priya", 55000, "JavaScript")
mgr = Manager("Rahul", 80000, 10)

print(dev1)
print(dev2)
print(mgr)

for emp in [dev1, dev2, mgr]:
    emp.work()

dev1.salary = 60000
print(f"updated: {dev1}")

dev1.salary = -1000
print(f"still: {dev1}")

dev3 = Developer("Jay", 50000, "Python")
print(f"dev1 == dev3? {dev1 == dev3}")
