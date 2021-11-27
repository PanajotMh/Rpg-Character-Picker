import time

print("Welcome to the RPG Charachter picker and storyline! V2.00\n")
time.sleep(2)
print("I will ask you 3 questions! Answer them correctly and i'll pick a character for you!\n")
time.sleep(3)
print("Here is an example: What pet do you want? 'Dog' 'Duck' or 'Cat'\n")
time.sleep(2)
print("Okay lets start!\n")
time.sleep(1)

Choices = []
Match_found = False
while not Match_found:  # Start a while loop to check if they found their match or not.
    Weapon_correct = False
    while not Weapon_correct:  # starts a while loop to check if they inputted the right weapon.
        weapon = str(input("What weapon do you want to use? 'Sword','Dagger','Bow' or 'Staff'\n"))
        Weapon = weapon.lower()
        Weapon = Weapon.capitalize()
        if Weapon == 'Sword' or Weapon == 'Dagger' or Weapon == 'Bow' or Weapon == 'Staff':
            print("\nOkay you picked " + Weapon + ".")
            Weapon_correct = True
        elif Weapon.isdigit():
            print("\nNo numbers! Please enter in a weapon!\n")
            time.sleep(2)
        else:
            print("\nNo such weapon found!\n")
            time.sleep(2)
    Choices.append(Weapon)

    Companion_correct = False
    while not Companion_correct:
        print("")
        companion = str(input("What companion do you want? 'Bear' 'Jaguar' or 'Owl'"))
        Companion = companion.lower()
        Companion = Companion.capitalize()
        if Companion == 'Bear' or Companion == 'Jaguar' or Companion == 'Owl':
            print("\nOkay you picked " + Companion + ".")
            Companion_correct = True
        elif Companion.isdigit():
            print("\nNo numbers! Please enter in a companion!")
            time.sleep(2)
        else:
            print("\nNo such companion found!")
            time.sleep(2)

    Choices.append(Companion)

    Armour_correct = False
    while not Armour_correct:
        armour = input("\nWhat armour do you want? 'Metal' or 'Leather'\n")
        Armour = armour.lower()
        Armour = Armour.capitalize()
        if Armour == 'Metal' or Armour == 'Leather':
            print("\nOkay you picked " + Armour + ".")
            Armour_correct = True
        elif Armour.isdigit():
            print("\nNo numbers! Please enter in a type of armour!")
            time.sleep(2)
        else:
            print("\nNo such armour found!")
            time.sleep(2)

    Choices.append(Armour)

    if Weapon == 'Sword' or Weapon == 'Dagger' and Companion == 'Bear' or Companion == 'Jaguar' and Armour == 'Metal':
        print("\nYour perfect match is a warrior!\n")
        time.sleep(2)
        print("\nA warrior charges forward with heart and attacks! Great choice!\n")
        Character_picked = "Warrior"
        time.sleep(2)
        Match_found = True
    elif Weapon == 'Staff' and Companion == 'Owl' and Armour == 'Leather':
        print("\nYour perfect match is a healer!\n")
        time.sleep(3)
        print("\nA healer stays back and heals his teammates during fight! Great choice!\n")
        Character_picked = "Healer"
        time.sleep(4)
        Match_found = True
    elif Weapon == 'Dagger' and Companion == 'Owl' and Armour == 'Leather':
        print("\nYour perfect match is a rogue assassin!\n")
        time.sleep(3)
        print(
            "An assassin has strong stealth skills, and specialises in defeating an enemy without becoming involved "
            "in a protracted melee.\n")
        Character_picked = "Rogue assassin"
        time.sleep(7)
        Match_found = True
    elif Weapon == 'Bow' and Companion == 'Owl' or Companion == 'Jaguar' and Armour == 'Leather':
        print("\nYour perfect match is a Ranger!\n")
        time.sleep(3)
        print("A ranger stays back with a bow and shoots arrows.Great choice!\n")
        time.sleep(2)
        Character_picked = 'Ranger'
        Match_found = True
    else:
        print("\nOh no,I wasn't able to find a match for you!\n")
        time.sleep(2)
        print("Let's try again\n")
        time.sleep(4)
        Choices.remove(Weapon)
        Choices.remove(Companion)
        Choices.remove(Armour)

Colours = ['Blue', 'Red', 'Orange', 'Yellow', 'Green', 'Violet', 'Black', 'Purple', 'White']
print("""\nAll right well done for finding your match! You had chosen """ + Weapon + """ as your weapon.
""" + Companion + """ as your companion and
""" + Armour + """ as your armour.\n""")
time.sleep(3)

Name = input("Now im going to make a super cool user name for you! What is your name?\n")
time.sleep(2)

Colours: list = ['Red', 'Blue', 'Yellow', 'Black', 'White', 'Orange', 'Green', 'Purple', 'Violet', 'Cyan', 'Pink', 'Indigo']
Favourite_Colour_Found = False
while not Favourite_Colour_Found:
    FavouriteColour = input("\nOkay " + Name + " what's your favourite colour?\n")
    Favcolour = FavouriteColour.lower()
    Favcolour = Favcolour.capitalize()
    if Favcolour in Colours:
        print("\nOkay you chose " + Favcolour + ".\n")
        Favourite_Colour_Found = True
        Character_Name: str = Name[:3] + Favcolour[3:]

    elif Favcolour.isdigit():
        print("\nNo digits please enter in a colour!\n")
    else:
        print("\nNo such colour found!\n")
time.sleep(2)

print("Your character name is " + Character_Name + ". Well done!\n")
time.sleep(2)
