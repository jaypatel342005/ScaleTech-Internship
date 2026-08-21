t = (1,)
x = (1)
print(type(t))
print(type(x))


t = (10, 20, 30, 40, 50)
# t[0] = 99  # TypeError

d = {
    (1, 2): "val1",
    (3, 4): "val2"
}
print(d[(1, 2)])


t = (1, 2, 3, 2, 2, 4)
print(t.count(2))
print(t.index(3))


a, b, c = (10, 20, 30)
print(a, b, c)

first, *rest = (1, 2, 3, 4, 5)
print(first)
print(rest)


t1 = ([1, 2, 3], 2, 3)
t1[0].append(4)
print(t1)


import copy

t2 = (1, 2, [3, 4])
t3 = copy.copy(t2)
t4 = copy.deepcopy(t2)

t2[2].append(5)

print(t2)
print(t3)
print(t4)


t5 = (1, 2) + (3, 4)
print(t5)

t6 = ("hi",) * 3
print(t6)
