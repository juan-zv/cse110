items = []
prices =  []
item = ""
item_price = ""
i = 0
action = None


while action != "5":

    print("\nWelcome to the Shopping Cart Program!\n")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("\nPlease enter an action: ")

    if action == "1":
        add_item = input("\nWhat item would you like to add? ")
        items.append(add_item)
        add_price = (input(f"What is the price of {add_item}? "))
        prices.append(add_price)
        print(f"{add_item} has been added to the cart.")
    elif action == "2":
        for i in range(len(items)):
            items = items[i]
            prices = prices[i]
            indexer = i + 1
            print(f"\n{indexer}. {items} - ${prices}")
    elif action == "3":
        remover = int(input("Which item would you like to remove? ")) - 1
        items.remove(item[remover])
        prices.remove(item_price[remover])
    elif action == "4":
        prices_total = sum(prices)
        print(f"The total price of the items in the shopping cart is {prices_total}")

print("Thank you. Goodbye.")



    