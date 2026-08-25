from functools import reduce, partial, lru_cache, cache
from collections import Counter, defaultdict
from itertools import combinations

# reduce
nums = [1, 2, 3, 4]
res = reduce(lambda x, y: x + y, nums)
print(res)

# reduce with multiplication (factorial)
fact = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(fact)

# reduce with initial value
res = reduce(lambda x, y: x + y, [1, 2, 3], 10)
print(res)


# partial
def power(base, exp):
    return base**exp

square = partial(power, exp=2)
print(square(5))

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
print(double(10))
print(double(20))

def send_msg(msg, prefix):
    print(prefix, msg)

warning = partial(send_msg, prefix="[WARNING]")
warning("low memory")
warning("connection failed")


# lru_cache
@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))
print(fib.cache_info())
fib.cache_clear()

@lru_cache(maxsize=100)
def fib2(n):
    if n <= 1:
        return n
    return fib2(n - 1) + fib2(n - 2)

print(fib2(30))

# cache (unlimited)
@cache
def fib3(n):
    if n <= 1:
        return n
    return fib3(n - 1) + fib3(n - 2)

print(fib3(40))


# practical combined example (order processing)
orders = [
    ("Jay", "Laptop"),
    ("Rahul", "Mouse"),
    ("Jay", "Keyboard"),
    ("Amit", "Laptop"),
    ("Jay", "Mouse"),
]

# count orders per customer
customers = [o[0] for o in orders]
print(Counter(customers))

# group products by customer
prods = defaultdict(list)
for customer, prod in orders:
    prods[customer].append(prod)
print(dict(prods))

# customer pairs
cust_list = list(prods.keys())
print(list(combinations(cust_list, 2)))
