# class and object
class Car:
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")


car1 = Car()
car1.start()
car1.stop()


# object is an instance of class
class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))
print(s1 is s2)


# instance attributes - different for every object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Jay", 21)
s2 = Student("Rahul", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)


# class attributes - shared by all objects
class Student:
    college = "ABC University"

    def __init__(self, name):
        self.name = name

s1 = Student("Jay")
s2 = Student("Rahul")

print(s1.college)
print(s2.college)


# methods
class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def study(self):
        print(f"{self.name} is studying {self.subject}")

    def introduce(self):
        print(f"hi, I'm {self.name}")

s = Student("Jay", "Python")
s.study()
s.introduce()


# self refers to current object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name}, age: {self.age}")

s1 = Student("Jay", 21)
s2 = Student("Rahul", 22)

s1.display()
s2.display()


# constructor __init__ - auto called on object creation
class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept
        print(f"employee '{self.name}' created!")

e1 = Employee("Jay", 50000, "IT")
e2 = Employee("Rahul", 60000, "HR")

print(f"{e1.name} works in {e1.dept}, earns Rs.{e1.salary}")
print(f"{e2.name} works in {e2.dept}, earns Rs.{e2.salary}")
