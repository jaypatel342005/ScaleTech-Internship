def greet(nm):
    print(f"hello {nm}!")

greet("Jay")


def add(a, b):
    return a + b

r = add(5, 3)
print(r)


def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(3, 3))


def total(*args):
    print(args)
    s = 0
    for n in args:
        s += n
    return s

print(total(1, 2, 3))


def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(name="Jay", age=21, city="Ahmedabad")


def mix(*args, **kwargs):
    print(args)
    print(kwargs)

mix(1, 2, 56, name="jay", id="23X1")


g = "i am global"

def test():
    l = "i am local"
    print(g)
    print(l)

test()

cnt = 0
def increment():
    global cnt
    cnt += 1

increment()
increment()
print("cnt:", cnt)

def outer():
    msg = "hello"
    def inner():
        nonlocal msg
        msg = "changed"
    inner()
    print(msg)

outer()


nums = [1, 2, 3, 4, 5]

sq = list(map(lambda x: x**2, nums))
print(sq)

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

names = ["Jay", "Meet", "Ravi"]
ages = [21, 22, 20]
print(list(zip(names, ages)))

for i, nm in enumerate(names):
    print(f"{i}: {nm}")

vals = [5, 2, 8, 1, 9]
print(sorted(vals))
print(sorted(vals, reverse=True))

print(min(vals))
print(max(vals))
print(sum(vals))

print(any([False, False, True]))
print(all([True, True, True]))


res = lambda a, b, c: a + b + c
print(res(1, 2, 3))

check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(12))
print(check(-12))
print(check(0))

students = [("Jay", 85), ("Meet", 92), ("Ravi", 78)]
students.sort(key=lambda s: s[1])
print(students)
