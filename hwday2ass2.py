# Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    print("You find a hidden treasure!")

# Task 2: Setting the Scene. Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You tripped over the treasure, fell into a pit and died of a stubbed toe!")

#Task 3: Default Path If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
if place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You tripped over the treasure, fell into a pit and died of a stubbed toe!")
    else:
        pass

#Task 4: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

menu = input("would you like human food or vegetarian food? ")
if menu == "vegetarian":
    print("Try Veggie Delight Caterers!")
else:
    print("Try Gourmet Meals Caterers!")



