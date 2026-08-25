from itertools import (
    permutations,
    combinations,
    combinations_with_replacement,
    product,
    chain,
    count,
    cycle,
    repeat,
    groupby,
)

# permutations (order matters)
items = ["A", "B", "C"]
res = list(permutations(items, 2))
print(res)


# combinations (order doesn't matter)
res = list(combinations(items, 2))
print(res)


# combinations with replacement
res = list(combinations_with_replacement("ABC", 2))
print(res)


# cartesian product
a = [1, 2]
b = ["A", "B"]
print(list(product(a, b)))

# product with repeat
res = list(product([0, 1], repeat=3))
print(res)


# chain - combine iterables
a = [1, 2, 3]
b = [4, 5]
c = [6, 7]
print(list(chain(a, b, c)))


# count - infinite counter
cnt = count(10)
print(next(cnt))
print(next(cnt))
print(next(cnt))

cnt_step = count(10, 2)
print(next(cnt_step))
print(next(cnt_step))


# cycle - repeat infinitely
colors = cycle(["Red", "Green", "Blue"])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))


# repeat
vals = list(repeat("Python", 3))
print(vals)


# groupby - group consecutive elements
data = [("CS", "Jay"), ("CS", "Rahul"), ("IT", "Amit"), ("IT", "Raj")]
for dept, students in groupby(data, key=lambda x: x[0]):
    print(dept, list(students))
