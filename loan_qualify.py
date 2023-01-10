# from operator import truediv


# print("Rate from 1-10:")
# loan=int(input("How large is the loan? "))
# credit_history=int(input("How good is your credit history? "))
# income=int(input("How high is your income? "))
# payment=int(input("How large is your down payment? "))
# if loan >= 5:
#     if credit_history and income >= 7:
#         print("Decision: yes")
#     elif payment >= 5:
#         print("Decision: yes")
#     else: print("Decision: no")
# elif credit_history < 4:
#     print("Decision: no")
# else:
#     if income and payment >=7:
#         print("Decision: yes")
#     elif income and payment >=4:
#         print("Decision: yes")
#     else: print("Decision: no")

print("Rate from 1-10:")
loan=int(input("How large is the loan? "))
credit_history=int(input("How good is your credit history? "))
income=int(input("How high is your income? "))
payment=int(input("How large is your down payment? "))

loan_result = True

if loan >= 5:
    if credit_history >=7 and income >= 7:
        loan_result = True
    elif credit_history >=7 or income >= 7:
        if  payment >= 5:
           loan_result = True
        else:
            loan_result = False
        
    else: loan_result = False
elif credit_history < 4:
    loan_result = False
else:
    if income >=7 or payment >=7:
        loan_result = True
    elif income >=4 and payment >=4:
        loan_result = True
    else: loan_result = False

if loan_result == True:
    print("The decision is yes.")
else: print("The decision is no.")