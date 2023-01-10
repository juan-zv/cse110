friends = []
friend_name = ""
while friend_name.lower() != "end":
    friend_name = input("Type the name of a friend ")
    if friend_name != "end":
        friends.append(friend_name)
print("\nYour friends are:")

for friend in friends:
    print(friend)
