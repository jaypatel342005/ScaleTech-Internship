age = 19

if age >= 18:
    print("you can vote")
else:
    print("too young")

marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"
    
print("grade:", grade)

x = 10
res = "even" if x % 2 == 0 else "odd"
print(res)


print("0 to 4")
for i in range(5):
    print(i)
    
nums = [1,2,3,4,5]
for n in nums:
    print(n)

for i in range(2, 10, 2):
    print(i)

for ch in "hello":
    print(ch)

i = 10
while i >= 0:
    print(i)
    i -= 1


for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass
    print(i)


for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
