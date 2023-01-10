age = int(input("What is the age of the first rider? "))
height = int(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider? ")
may_ride = False

if second_rider.lower() == "yes":
    second_age = int(input("What is the age of the second rider? "))
    second_height = int(input("What is the height of the second rider? "))
    if (age or second_age >= 18) and (height and second_height >= 36):
        may_ride = True
    elif (age and second_age < 18) and (age and second_age >= 12) and (height and second_height >= 36):
        may_ride = True
    elif (age or second_age >= 16) and (age or second_age >= 14) and (height and second_height >= 36):
        may_ride = True
    else:
        may_ride = False
else:
    if age >= 18 and height >= 62:
        may_ride = True
    elif age < 18 and age >= 12 and height >= 62:
        golden_passport = input("Do you have a golden passport? ")
        if golden_passport.lower() == "yes":
            may_ride = True
        else:
            may_ride = False
    else:
        may_ride = False


if may_ride == True:
    print("Welcome to the  ride. Please be safe and have fun!")
else: 
    print("Sorry, you may not ride")