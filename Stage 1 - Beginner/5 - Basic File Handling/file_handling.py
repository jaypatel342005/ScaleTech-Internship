f = open("data.txt", "r")
print(f.read())
f.close()

with open("data.txt", "r") as f:
    print(f.read())

with open("data.txt", "r") as f:
    print(f.readline())
    
with open("data.txt", "r") as f:
    print(f.readlines())


with open("data.txt", "w") as f:
    f.write("hello from python\n")
    f.write("second line\n")

with open("data.txt", "a") as f:
    f.write("appended line\n")

with open("data.txt", "r") as f:
    print(f.read())


with open("data.txt", "r") as f:
    f.seek(5)
    print(f.read())


with open("data.txt", "r") as f:
    print(f.name)
    print(f.mode)
    print(f.closed)


# csv
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    
    for row in reader:
        if len(row) >= 2:
            print(f"Name: {row[0]}, Age: {row[1]}")


data = [
    ["Name", "Age", "Role"],
    ["Jay", "21", "Intern"],
    ["Meet", "30", "Designer"]
]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


with open("data.csv", "w", newline="") as f:
    fields = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fields)
    
    writer.writeheader()
    writer.writerow({"Name": "Jay", "Age": 21, "City": "Morbi"})
    writer.writerow({"Name": "Ravi", "Age": 22, "City": "Surat"})
