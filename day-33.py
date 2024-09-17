d = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(d['name'])
print(d.get("name"))
print(d.keys())
print(d.values())
print(d.items())

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)