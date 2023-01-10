banks = []
acc_name = ""
balances = []
balance_ammount = None

while acc_name.lower() != "quit":
    acc_name = input("What is the name of this account? ")
    banks.append(acc_name)
    balance_ammount = float(input("What is the balance? "))
    balances.append(balance_ammount)

print("\nAccount Information: ")
for i in range(len(banks)):
    acc_name = banks[i]
    balance_ammount = balances[i]
    print(f"{acc_name} - ${balance_ammount}")