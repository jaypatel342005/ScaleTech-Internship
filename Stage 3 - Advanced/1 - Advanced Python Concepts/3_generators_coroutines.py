import asyncio


# ---- generators ----

# yield pauses the function and sends a value - execution resumes on next()
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1


for num in count_up(5):
    print(num)


# manually get values one at a time with next()
gen = count_up(3)
print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3


# generator expression uses () instead of [] - no list created in memory
nums_list = [x ** 2 for x in range(10)]   # stores all values
nums_gen = (x ** 2 for x in range(10))    # computes one at a time

print(type(nums_list))
print(type(nums_gen))

for v in nums_gen:
    print(v, end=" ")
print()


# generator for large data - only 1 value in memory at a time
def big_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


total = sum(big_range(1_000_000))
print("sum:", total)


# send() passes a value back INTO the generator
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


acc = accumulator()
next(acc)              # prime the generator (advance to first yield)
print(acc.send(10))    # 10
print(acc.send(20))    # 30
print(acc.send(5))     # 35


# generator pipeline - chain generators like a processing pipeline
def read_numbers():
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        yield n

def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square(numbers):
    for n in numbers:
        yield n ** 2

pipeline = square(filter_even(read_numbers()))
print(list(pipeline))   # [4, 16, 36, 64, 100]


# lazy file reader - reads one line at a time, avoids loading entire file into memory
def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


with open("sample.txt", "w") as f:
    f.write("line one\nline two\nline three\nline four\nline five")

for line in read_lines("sample.txt"):
    print(line)


def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

matches = filter_lines(read_lines("sample.txt"), "line t")
for m in matches:
    print("match:", m)


# ---- coroutines ----

# coroutine = async function - pauses at await, lets other tasks run
async def hello():
    print("starting task")
    await asyncio.sleep(1)
    print("task done")


asyncio.run(hello())


# coroutine that returns a value
async def fetch_price(item):
    await asyncio.sleep(0.5)
    prices = {"laptop": 50000, "phone": 30000}
    return prices.get(item, 0)


async def main():
    price = await fetch_price("laptop")
    print("price:", price)


asyncio.run(main())


# multiple coroutines running at the same time with gather
async def get_user(uid):
    await asyncio.sleep(0.3)
    return {"id": uid, "name": f"user_{uid}"}


async def load_users():
    users = await asyncio.gather(get_user(1), get_user(2), get_user(3))
    for u in users:
        print(u)


asyncio.run(load_users())


# async generator - generator that can also await
async def async_countdown(n):
    while n > 0:
        yield n
        await asyncio.sleep(0.2)
        n -= 1


async def use_async_gen():
    async for value in async_countdown(5):   # must use async for
        print(value)


asyncio.run(use_async_gen())


# generator vs coroutine
def number_gen():        # generator - produces values with yield
    yield 1
    yield 2

async def fetch_gen():   # coroutine - performs async work with await
    await asyncio.sleep(0)
    return "done"

for n in number_gen():
    print("gen:", n)

print(asyncio.run(fetch_gen()))


import os
os.remove("sample.txt")
