import math
import random
import datetime
import os
import re


print(math.sqrt(16))
print(math.factorial(5))
print(math.pi)
print(math.floor(3.7))
print(math.ceil(3.7))
print(math.pow(2, 3))


print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))

l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)

print(random.sample(range(1, 50), 5))
print(random.random())


now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))

today = datetime.date.today()
print(today)

tmr = today + datetime.timedelta(days=1)
print("tomorrow:", tmr)

dt = datetime.datetime.strptime("15-08-2025", "%d-%m-%Y")
print(dt)


print(os.getcwd())
print(os.listdir())

if not os.path.exists("test_dir"):
    os.mkdir("test_dir")

p = os.path.join("folder", "subfolder", "file.txt")
print(p)


# regex
txt = "404 not found"
m = re.search(r"\d+", txt)
if m:
    print(m.group())

txt = "Error 404 found"
print(re.match(r"\d+", txt))

txt2 = "404 Error found"
print(re.match(r"\d+", txt2).group())

txt3 = "my numbers are 123 and 456 and 789"
nums = re.findall(r"\d+", txt3)
print(nums)

txt4 = "222-333 and 555-444 is mobile number"
print(re.sub(r"\d{3}-\d{3}", "XXX-XXX", txt4))

m = re.search(r"(\d{3})-(\d{3})", txt4)
if m:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

txt5 = "one,two;three four"
print(re.split(r"[,;\s]+", txt5))

pattern = re.compile(r"\d{2,4}")
print(pattern.findall("age 20, year 2025, code 5"))

email = "jay@gmail.com"
if re.match(r"^[\w.+-]+@[\w-]+\.[\w.]+$", email):
    print(f"{email} is valid")

phone = "9876543210"
if re.match(r"^\d{10}$", phone):
    print(f"{phone} is valid phone")
