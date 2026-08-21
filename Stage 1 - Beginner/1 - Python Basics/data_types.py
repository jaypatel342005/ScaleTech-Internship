name = "Jay"
age = 21
pi = 3.14

a, b, c = 1, 2, 3
x = y = z = 0

a, b = b, a
print(a, b)


a = 10 
b = 3.14
c = 2 + 3j

print(type(a))
print(type(b))
print(type(c))

d = "Hello, World!"
print(type(d))

e = True
print(type(e))

f = [1, 2, 3, 4, 5]
g = (1, 2, 3, 4, 5)
h = {1, 2, 3, 4, 5}

print(type(f))
print(type(g))
print(type(h))

i = {"name": "Jay", "age": 21}
print(type(i))

j = bytes([65, 66, 67]) 
print(j, type(j))

k = None
print(type(k))


x = "100"
y = int(x)
z = float(x)
print(y, z)

n = 10
s = str(n)
print(s, type(s))

print(bool(0))
print(bool(""))
print(bool(1))
print(bool("hi"))


print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 3)

print(5 == 5)
print(5 != 3)
print(5 > 3)

print(True and False)
print(True or False)
print(not True)

a = [1,2]
b = [1,2]
print(a == b)
print(a is b)

fruits = ["apple", "mango", "banana"]
print("mango" in fruits)
print("grape" not in fruits)

x = 10
x += 5
x -= 3
x *= 2
x //= 5
print(x)


# nm = input("name? ")
# ag = int(input("age? "))

nm = "Jay"
ag = 21
print("name: %s, age: %d" % (nm, ag))
print("name: {}, age: {}".format(nm, ag))
print(f"name: {nm}, age: {ag}")

print("a", "b", "c", sep="-")
print("hello", end=" ")
print("world")
