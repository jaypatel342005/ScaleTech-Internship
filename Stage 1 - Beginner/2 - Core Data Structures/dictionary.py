d = {
    "name": "Jay",
    "age": 21
}

print(d["name"])
print(d.get("name", "not found"))
print(d.get("email", "not found"))

d["name"] = "Jay Patel"
d["id"] = "23X1"
print(d)

print(d.keys())
print(d.values())
print(d.items())

for k, v in d.items():
    print(f"{k} -> {v}")

d.pop("id")
print(d)

d.setdefault("city", "Morbi")
print(d)


extra = {"email": "jay@gmail.com", "age": 22}
d.update(extra)
print(d)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = d1 | d2
print(d3)


students = {
    "s1": {"name": "Jay", "marks": 85},
    "s2": {"name": "Meet", "marks": 92}
}

print(students["s1"]["name"])

for sid, info in students.items():
    print(f"{sid}: {info['name']} scored {info['marks']}")


fruits = {"apple": 2.00, "orange": 3.00, "banana": 2.30}
doubled = {f: p * 2 for f, p in fruits.items()}
print(doubled)

keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))
print(d)
