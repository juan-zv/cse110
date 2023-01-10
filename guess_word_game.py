word = "Brass Plates"
counter = 0

print("Welcome to the word guessing game!\n")
guess = input("What is your guess? ") 

while guess.lower() != word.lower():
    for letter in guess:
        if letter.lower() == word.lower():  #I think this is not well conditioned. I couldn't find a way to compare each letter from a word.
            hint = letter                   #I am not sure this has sense or will store each letter from the guess word.
        else:
            hint = ""   
    print(f"Your hint is {hint}")           #This always displays the else result, unless you enter the correct
    counter = counter +1                    #word which actually jumps to the end, the congratulations message.
    guess = input("What is your guess? ")


print("Congratulations you guessed it!")
print(f"It took you {counter} guesses.")
