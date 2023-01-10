print("----------------------------- ADVENTURE GAME -----------------------------")

print("You wake up at the middle of a desert, you don't remember how you got there. It is really hot and dry.")
a = input("There is a bag pack next to you. Do you want to OPEN to see what's inside or IGNORE it's content?\n")
if a.lower() == "open":
    print("You see there is a gun and some bullets for it, a lantern and a satellite phone. You pick the bag up with everything and start walking towards a mountain you see far away.\nThe heat is really uncomfortable and you wish there was a place to stop and maybe find a Wi-Fi connection or signal for your phone.")
    a1 = input("You step up to a cottage with a 'Keep Away' sign. Do you want to GO AWAY or ENTER?\n")
    if a1.lower() == "go away" and "goaway":
        print("You chose right, you don't want to find something weird or rare, but you just want to find a way home.You pass straight the cottage towards the shadow of the mountain.")
        a1_1 = input("After walking for some minutes you reach the base of the mountain. Do you want to CLIMB it or REST, or maybe try to LOOK for other way?\n")
        if a1_1.lower() == "climb":
            print("Wow you decided to climb even though you haven't drank water for a while. You start to climb but get tired and faint. You fall down the mountain.")
        elif a1_1.lower() == "rest":
            print("You rest in the shadow and start to sleep. You realize it's cold and wake up. It is really dark and there are many scorpions surrounding you.")
        elif a1_1.lower() == "look":
            print("You try to look for another place to rest or climb and go to the left. You see far away and there is a car-shaped shadow far away. There might be someone there!")
        else:
            print("You should have chose an option!\ ----------------------- The End lol -----------------------")
    elif a1.lower() == "enter":
        print("You enter and see just one row of escalators going down. The place is curiously clean and well iluminated.")
        a1_2 = input("There must be something at the end of the stairs. Do you want to TAKE the scalators, SHOUT to see if someone is there, or EXIT the cottage?\n")
        if a1_2.lower() == "take":
            print("You arrive to the end and see a door with a fingerprint scanner. It is locked and maybe there's someone on the other side. You knock.")
        elif a1_2.lower() == "exit":
            print("That was pretty weird. What was doing that in the middle of nothing? Is this maybe a hidden place from the government?")
        elif a1_2.lower() == "shout":
            print("There is a lot of echo when you shout and see that no one is answering. Suddenly you hear like a door being opened.")
        else:
            print("You should have chose an option!\ ----------------------- The End lol -----------------------")
    else:
        print("You should have chose an option!\ ----------------------- The End lol -----------------------")
elif a.lower() == "ignore":
    print("You pick the bag up and start walking towards a mountain you see far away.\nThe heat is really uncomfortable and you wish there was a place to stop and maybe find a way to contact anybody. The bag is heave and you dont want to carry it.")
    a2 = input("You want to LEAVE the bag or CARRY it?\n")
    if a2.lower() == "leave":
        print("It's fine you didn't even need it. You are lighter now and feel better as you don't need to carry something heavy.")
        print("There is a kind of cottage in the distance. You just threw away the bag, you need help and maybe there's something or someone there.")
        a2_1 = input("You reach the cottage, theres a 'Keep Away' sign. Do you want to ENTER or SEARCH the surroundings for something more? Or maybe KNOCK the door?\n")
        if a2_1.lower() == "enter":
             print("You enter the cottage and see there are footprints. There seem recent so you follow them to look for help.")
        elif a2_1.lower() == "search":
             print("You walk arround the cottage and discover a car parked some feet away. You see footprints towards the cottage.")
        elif a2_1.lower() == "knock":
             print("You knock in order to see if someone's there but after 15 min, you realize you just have to enter. But it's always good to be polite.")
        else:
             print("You should have chose an option!\ ----------------------- The End lol -----------------------")
    elif a2.lower() == "carry":
        print("Why would you carry it? It is really heavy and you don't even know whats inside... That is kind of scary.")
        a2_2 = input("Do you want to OPEN it now or WAIT until it's necesary?\n")
        if a2_2.lower() == "open":
            print("You see there are bullets, a gun for them and some survival gadgets. That's really useful. You are ready for what can come up to you.")
        elif a2_2.lower() == "wait":
            print("You start walking and see a car moving in the distance. You move you arms asking for help and the car changes direction towards you.")
        else:
            print("You should have chose an option!\ ----------------------- The End lol -----------------------")
    else:
        print("You should have chose an option!\ ----------------------- The End lol -----------------------")
else : print("You should have chose an option!\ ----------------------- The End lol -----------------------")