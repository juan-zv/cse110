people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 100
youngest_name = ""

for line in people:
    splitted = line.split()
    name = splitted[0]
    age = int(splitted[1])

    if age < youngest:
        youngest = age
        youngest_name = name

# print(name)
# print(age)
print(youngest)
print(youngest_name)