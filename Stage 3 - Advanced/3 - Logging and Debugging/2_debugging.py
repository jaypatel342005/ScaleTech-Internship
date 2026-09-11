import pdb
import logging

# 3 types of bugs:
# syntax error  - python wont run
# runtime error - crashes while running
# logic error   - runs but gives wrong answer


def add(a, b):
    result = a + b
    # pdb.set_trace()   # uncomment to pause and inspect
    return result

print(add(10, 20))


# breakpoint() is same as pdb.set_trace() but cleaner
def multiply(a, b):
    result = a * b
    # breakpoint()
    return result

print(multiply(4, 5))


# logic error example - wrong formula but no crash
def area_wrong(length, width):
    return length + width   # should be *

def area(length, width):
    return length * width

print(area_wrong(5, 3))   # 8 - wrong
print(area(5, 3))         # 15 - correct


# runtime error
def average(numbers):
    return sum(numbers) / len(numbers)

try:
    print(average([10, 20, 30]))
    print(average([]))
except ZeroDivisionError:
    print("empty list, cant divide")


# nested call crash - traceback shows the full path
def save():
    x = 10 / 0

def process():
    save()

def run():
    process()

try:
    run()
except ZeroDivisionError as e:
    print("crash:", e)


# pdb commands in the terminal prompt:
# n  = next line
# s  = step into function
# c  = continue
# p x = print value of x
# l  = show code around current line
# w  = show call stack
# q  = quit


# conditional breakpoint - in vs code right click the red dot and add condition
# useful when you only want to stop at a specific loop iteration
for i in range(10):
    result = i * 2
    pass   # add breakpoint here with condition i == 7


# logging helps trace bugs too
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def divide(a, b):
    logging.debug(f"a={a} b={b}")
    if b == 0:
        logging.error("b is zero")
        raise ValueError("cant divide by zero")
    result = a / b
    logging.info(f"result={result}")
    return result


try:
    print(divide(10, 2))
    print(divide(10, 0))
except ValueError:
    logging.exception("divide crashed")


# vs code debugger steps:
# click line number to add breakpoint (red dot)
# press F5 to start
# F10 = step over  F11 = step into  shift+F11 = step out  F5 = continue
# left panel shows all variable values while paused
