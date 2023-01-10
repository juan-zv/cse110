grade = float(input("What is your grade percentage for your class? "))

letter = ''

sign = ""

if grade >= 90 :
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

if (grade % 10 >= 7 or grade % 10 == 0) and letter not in ('A', 'F') :
    sign = "+"
elif grade % 10 < 3 and letter not in ("F"):
    sign ="-"
else:
    sign =""

print(f'Your letter grade: {letter} {sign}')

if grade >= 70:
    print("\nCongratulations, you passed!")
else:
    print("Sorry, you failed, but keep working hard!")