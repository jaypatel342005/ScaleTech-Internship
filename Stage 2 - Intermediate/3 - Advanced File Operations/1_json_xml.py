import json
import os
import xml.etree.ElementTree as ET

DIR = os.path.dirname(os.path.abspath(__file__))

# ---- JSON ----

# json.loads() - json string -> python object
data = '{"name": "Jay", "age": 21}'
student = json.loads(data)
print(student)
print(student["name"])


# json.dumps() - python object -> json string
student = {"name": "Jay", "age": 21, "skills": ["Python", "Java"]}
s = json.dumps(student)
print(s)

# with indent
s = json.dumps(student, indent=4)
print(s)


# json.dump() - write python object to json file
student = {
    "name": "Jay",
    "age": 21,
    "skills": ["Python", "Java", "SQL"]
}

with open(os.path.join(DIR, "student.json"), "w") as f:
    json.dump(student, f, indent=4)


# json.load() - read json file -> python object
with open(os.path.join(DIR, "student.json"), "r") as f:
    data = json.load(f)

print(data)
print(data["name"])
print(data["skills"][0])


# nested json
nested = {
    "name": "Jay",
    "contact": {
        "email": "jay@example.com",
        "phone": "9876543210"
    },
    "skills": ["Python", "Java", "SQL"]
}

with open(os.path.join(DIR, "student.json"), "w") as f:
    json.dump(nested, f, indent=4)

with open(os.path.join(DIR, "student.json"), "r") as f:
    data = json.load(f)

print(data["contact"]["email"])
print(data["skills"][0])


# json list
students = [
    {"id": 1, "name": "Jay"},
    {"id": 2, "name": "Rahul"},
    {"id": 3, "name": "Amit"},
]

with open(os.path.join(DIR, "students.json"), "w") as f:
    json.dump(students, f, indent=4)

with open(os.path.join(DIR, "students.json"), "r") as f:
    data = json.load(f)

for s in data:
    print(s["id"], s["name"])


# json error handling
raw = '{"name": "Jay", "age": 21'
try:
    result = json.loads(raw)
except json.JSONDecodeError:
    print("invalid json")


# ---- XML ----
# Extensible Markup Language
# create xml file
student_xml = """<student id="101">
    <name>Jay</name>
    <age>21</age>
    <skills>
        <skill>Python</skill>
        <skill>Java</skill>
        <skill>SQL</skill>
    </skills>
</student>"""

with open(os.path.join(DIR, "student.xml"), "w") as f:
    f.write(student_xml)


# parse xml
tree = ET.parse(os.path.join(DIR, "student.xml"))
root = tree.getroot()

print(root.tag)
print(root.attrib)
print(root.attrib["id"])


# access elements
print(root.find("name").text)
print(root.find("age").text)


# loop through child elements
skills = root.find("skills")
for skill in skills:
    print(skill.text)


# multiple students xml
students_xml = """<students>
    <student id="1"><name>Jay</name></student>
    <student id="2"><name>Rahul</name></student>
    <student id="3"><name>Amit</name></student>
</students>"""

with open(os.path.join(DIR, "students.xml"), "w") as f:
    f.write(students_xml)

tree = ET.parse(os.path.join(DIR, "students.xml"))
root = tree.getroot()

for s in root.findall("student"):
    print(s.attrib["id"], s.find("name").text)


# create xml with python
root = ET.Element("student")

name = ET.SubElement(root, "name")
name.text = "Jay"

age = ET.SubElement(root, "age")
age.text = "21"

tree = ET.ElementTree(root)
tree.write(os.path.join(DIR, "new_student.xml"))
