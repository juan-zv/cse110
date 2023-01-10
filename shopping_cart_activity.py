items = []
item = ""
prices = []
item_price = None
enumerator = 0

while item.lower() != "quit":
    item = input("What item would you like to add? ")
    items.append(item)
    item_price = input(f"What is the price of {item}? ")
    prices.append(item_price)

print("The content of the shopping car are:")
for item in items:
    enumerator = enumerator + 1
    print(f"{enumerator}. {item} - ${item_price}") #round 2 decimals no funciona el item_price