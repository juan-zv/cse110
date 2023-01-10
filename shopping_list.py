items = []
item = ""

while item != "quit":
    for item in items:
        item = input("Please enter the items of the shopping list (type: quit to finish):")
        items.append(item)

print("The shopping list is: ")
for i in range(len(items)):
    item = items[i]
    print(item)