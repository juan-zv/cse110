# word = "Commitment"
# fav_letter = input("What is your favourite letter? ")
# for letter in word:
#     if letter == fav_letter.lower():
#         print("_" , end="")
#     else:
#         print(letter, end="")

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
i = input("Please enter a number ")
for i, letter in enumerate(quote):
    print(letter.capitalize(), end="")