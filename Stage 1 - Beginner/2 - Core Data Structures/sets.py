enrolled = {101, 102, 103, 104, 105, 105}
print(enrolled)

enrolled.add(106)
print(enrolled)

# enrolled.remove(999)  # KeyError
enrolled.discard(103)
print(enrolled)

enrolled.pop()
print(enrolled)


sem6 = {101, 102, 103, 104, 105}
sem5 = {104, 105, 106, 107, 108}

print(sem6 | sem5)
print(sem6 & sem5)
print(sem6 - sem5)
print(sem6 ^ sem5)

toppers = {101, 102}
print(toppers.issubset(sem6))
print(sem6.issuperset(toppers))


sq = {x**2 for x in range(1, 6)}
print(sq)


fixed = frozenset([101, 102, 103])
# fixed.add(104)  # error
print(fixed)
