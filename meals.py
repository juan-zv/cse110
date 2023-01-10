currencytype= str(input("Which currency will you use? "))
child_meal= float(input("What is the price of a child's meal? "))
adult_meal= float(input("What is the price of an adult's meal? "))
child= int(input("How many children are there? "))
adults= int(input("How many adults are there? "))
tax= int(input("What is the sales tax rate? "))
discount= float(input("How much is your discount coupon? "))


subt= (child_meal*child) + (adult_meal*adults)
salestax= (tax/100)*subt
total= subt + salestax + discount

print(f"\nSubtotal: {subt: .2f} {currencytype}")
print(f"Sales Tax: {salestax: .2f} {currencytype}")
print(f"Discount: {discount: .2f} {currencytype}")
print(f"Total: {total: .2f} {currencytype}")

payamount= float(input("\nWhat is the payment amount? "))
print(f"Change: {(payamount-total): .2f} {currencytype}")