try:
    n = int(input("Enter a number: "))
    print(f"you entered: {n}")
except ValueError as e:
    print("Invalid input!", e)


try:
    x = 10 / 0
except ZeroDivisionError:
    print("cant divide by zero!")
except Exception as e:
    print("something went wrong:", e)


try:
    num = int("42")
except ValueError:
    print("bad value")
else:
    print("no errors! num =", num)
finally:
    print("this always runs")


def div(a, b):
    if b == 0:
        raise ValueError("b should not be zero")
    return a / b

try:
    print(div(10, 0))
except ValueError as e:
    print("caught:", e)


def calc_avg(marks):
    assert len(marks) > 0, "marks list cant be empty"
    return sum(marks) / len(marks)

print(calc_avg([80, 90, 70]))
# print(calc_avg([]))  # AssertionError


class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 18 and 100"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.msg} : provided age = {self.age}"

try:
    raise InvalidAgeError(12)
except InvalidAgeError as e:
    print(f"Error: {e}")
