s = "0123456789"

print(s[0])
print(s[-1])
print(s[1:3])
print(s[1:])
print(s[:4])
print(s[:])
print(s[::2])
print(s[1::2])
print(s[::-1])


s = "Hello, World!"
# s[0] = "h"  # TypeError

s = "Hello, World!"
print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("World", "Universe"))
print(s.split(","))
print(s.find("World"))
print(s.count("l"))
print(s.startswith("Hello"))
print(s.endswith("!"))

txt = "hello world"
print(txt.title())

print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())


words = ["I", "am", "learning", "python"]
print(" ".join(words))
print("-".join(words))


msg = """this is
a multiline
string"""
print(msg)

path = r"C:\new\test"
print(path)


nm = "Jay"
ag = 21
print("My name is {} and I am {} years old.".format(nm, ag))
print(f"My name is {nm} and I am {ag} years old.")

price = 49.567
print(f"price: {price:.2f}")


txt = "hello"
encoded = txt.encode("utf-8")
print(encoded)
print(encoded.decode())
