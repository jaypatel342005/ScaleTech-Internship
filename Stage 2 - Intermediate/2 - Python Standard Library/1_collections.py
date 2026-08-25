from collections import Counter, defaultdict, deque

# counter - basic usage
nums = [1, 2, 2, 3, 3, 3, 4]
c = Counter(nums)
print(c)

# counter with string
text = "banana"
c = Counter(text)
print(c)
print(c["a"])

# counter with words
sentence = "python java python c java python"
words = sentence.split()
c = Counter(words)
print(c)

# most_common
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
c = Counter(nums)
print(c.most_common(2))
print(c.most_common())

# elements
c = Counter({"a": 3, "b": 2})
print(list(c.elements()))

# counter arithmetic
c1 = Counter({"x": 3, "y": 2})
c2 = Counter({"x": 1, "y": 4})
print(c1 + c2)
print(c1 - c2)

# character frequency
text = "programming"
freq = Counter(text)
for ch, count in freq.items():
    print(ch, count)


# defaultdict with int
d_int = defaultdict(int)
d_int["apple"] += 1
d_int["apple"] += 1
d_int["banana"] += 1
print(d_int)

# defaultdict with list (grouping)
d_list = defaultdict(list)
d_list["CS"].append("Jay")
d_list["CS"].append("Rahul")
d_list["IT"].append("Amit")
print(d_list)

# defaultdict with set
d_set = defaultdict(set)
d_set["CS"].add("Python")
d_set["CS"].add("Java")
d_set["CS"].add("Python")
print(d_set)


# deque - double ended queue
q = deque()
q.append("A")
q.append("B")
q.append("C")
print(q)

q.appendleft("X")
print(q)

q.pop()
print(q)

q.popleft()
print(q)

# queue (FIFO)
q = deque()
q.append("person 1")
q.append("person 2")
q.append("person 3")
print(q.popleft())
print(q.popleft())

# stack (LIFO)
st = deque()
st.append(10)
st.append(20)
st.append(30)
print(st.pop())

# deque rotate
d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print(d)
d.rotate(-2)
print(d)

# deque maxlen
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print(d)
d.append(4)
print(d)
