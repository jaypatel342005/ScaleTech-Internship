l = ["Jay", 20, 3.14, True, [1, 2, 3], 4+5j, None]

l[0] = "Jay Patel"
print(l)

print(len(l))

l.append("77")
print(l)

print(l.pop())
print(l)

l.insert(0, "hello")
print(l)

l.extend([1, 2, 3])
print(l)

l.remove(2)
print(l)

# print(l.sort())  # error cant sort mixed types
print(l.sort(key=str))
print(l)
print(l.reverse())
print(l)


l1 = [1, 2, 3]
l2 = l1

l1.insert(0, 0)
print("l1 =", l1)
print("l2 =", l2)
print(l1 is l2)


l1 = [1, 2, 3, 4, 5]
l2 = [x**2 for x in l1]
l3 = [x for x in l1 if x % 2 == 0]

print(l2)
print(l3)


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(m[1][2])


nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[1:6:2])
print(nums[::-1])

res = [x * 2 if x % 2 == 0 else x for x in range(5)]
print(res)


a, b, c = [10, 20, 30]
print(a, b, c)

first, *rest = [1, 2, 3, 4, 5]
print(first)
print(rest)


fruits = ["apple", "mango", "banana"]
for i, f in enumerate(fruits):
    print(f"{i}: {f}")


grid = [[]] * 3
grid[0].append(5)
print(grid)

grid = [[] for _ in range(3)]
grid[0].append(5)
print(grid)


# shallow vs deep copy
import copy

l1 = [[1, 2, 3], 1, 2, 3]
l2 = l1[:]
l3 = l1.copy()
l4 = copy.deepcopy(l1)

l1[1] = 99
l1[0][0] = 99

print("l1:", l1)
print("l2:", l2)
print("l3:", l3)
print("l4:", l4)


d1 = {"name": "Jay", "marks": [90, 85, 78]}
d2 = d1.copy()
d3 = copy.deepcopy(d1)

d1["marks"].append(95)
d1["name"] = "Meet"

print("d1:", d1)
print("d2:", d2)
print("d3:", d3)
