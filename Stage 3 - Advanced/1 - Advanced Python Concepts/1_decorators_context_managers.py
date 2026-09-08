import time
from functools import wraps


# ---- decorators ----

def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper


@my_decorator
def greet():
    print("hello")


greet()


# *args, **kwargs let the decorator work with any function arguments
def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("starting")
        result = func(*args, **kwargs)
        print("done")
        return result
    return wrapper


@my_decorator2
def add(a, b):
    return a + b


print(add(3, 7))


# @wraps keeps the original function name and docs intact
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished {func.__name__}")
        return result
    return wrapper


@logger
def multiply(a, b):
    return a * b


print(multiply(4, 5))
print(multiply.__name__)


# timer decorator - measures how long a function takes
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper


@timer
def slow_task():
    time.sleep(0.5)
    return "done"


print(slow_task())


# validation decorator - rejects bad inputs before calling the function
def positive_only(func):
    @wraps(func)
    def wrapper(a, b):
        if a < 0 or b < 0:
            raise ValueError("arguments must be positive")
        return func(a, b)
    return wrapper


@positive_only
def divide(a, b):
    return a / b


print(divide(10, 2))
try:
    divide(-5, 2)
except ValueError as e:
    print(e)


# stacking decorators - inner decorator runs first, then outer
@timer
@logger
def compute(n):
    return sum(range(n))


print(compute(1000))


# ---- context managers ----

# class-based context manager
# __enter__ runs on entering 'with', __exit__ runs on leaving (even on error)
class FileManager:

    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"closing {self.filename}")
        if self.file:
            self.file.close()
        return False


with FileManager("test_ctx.txt", "w") as f:
    f.write("hello context manager")

with FileManager("test_ctx.txt", "r") as f:
    print(f.read())


# @contextmanager - simpler way using yield
# code before yield = setup, code after yield = cleanup
from contextlib import contextmanager


@contextmanager
def timer_ctx(label):
    print(f"[{label}] starting")
    start = time.time()
    yield
    print(f"[{label}] finished in {time.time() - start:.4f}s")


with timer_ctx("database query"):
    time.sleep(0.3)


# context manager with error handling
@contextmanager
def safe_open(filename, mode="r"):
    f = None
    try:
        f = open(filename, mode)
        yield f
    except FileNotFoundError:
        print(f"file not found: {filename}")
        yield None
    finally:
        if f:
            f.close()


with safe_open("test_ctx.txt") as f:
    if f:
        print(f.read())

with safe_open("missing.txt") as f:
    if f:
        print(f.read())


# db transaction - commit if success, rollback on error
class FakeDB:
    def execute(self, sql):
        print(f"executing: {sql}")
    def commit(self):
        print("committed")
    def rollback(self):
        print("rolled back")


@contextmanager
def transaction(db):
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise


db = FakeDB()

with transaction(db) as conn:
    conn.execute("INSERT INTO users VALUES (1, 'Jay')")

try:
    with transaction(db) as conn:
        conn.execute("INSERT INTO users VALUES (2, 'Rahul')")
        raise RuntimeError("something failed")
except RuntimeError:
    pass

import os
os.remove("test_ctx.txt")
