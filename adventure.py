import os
# display the menu
os.system('clear')
print("Text Adventure by AI")
print("--------------------")
print("1. New Quest")
print("2. Load Quest")
print("3. Exit")

# get the player's choice
choice = input("Enter the number of your choice: ")

# handle the player's choice
if choice == "2":
  os.system('clear')
  # load a saved quest
  # load the character data from the char.data file
  try:
    with open("savedata/char.data", "r") as file:
      data = file.read()
  except:
    print("Error: Save file not found or corrupt. Please start a new quest.")
    exit()

  # parse the character data
  name, character_class = data.split(",")

  # use the character data in the game
  print("Welcome back, " + name + " the " + character_class + "!")

  # (insert code here to resume the gameplay using the loaded character data)


elif choice == "1":
  os.system('clear')
  # start a new quest
  # prompt the user for their name
  name = input("What is your name, adventurer? ")
  os.system('clear')
  # use the name in the game
  print("Welcome to the medieval world, " + name + "!")

  # background story
  print("As you enter the medieval world, you are immediately struck by its beauty and grandeur. The rolling hills, lush forests, and sparkling streams all combine to create a magical atmosphere.")
  print("You are a brave adventurer, known throughout the land for your skills and bravery. You have been called upon to embark on a quest to defeat the evil sorcerer who has been terrorizing the kingdom.")
  print("The sorcerer is rumored to be hiding in an ancient castle, deep in the heart of the dark forest. It is said that only a true hero can defeat the sorcerer and save the kingdom.")
  print("You must journey to the castle, face the sorcerer, and vanquish him once and for all. Are you ready for this epic quest? Will you be able to save the kingdom and become a hero? Only time will tell.")
  print("Good luck on your journey, adventurer! May the gods be with you.")

  # prompt the player to choose their character class
  print("")
  print("Please choose your character class:")
  print("1. Sorcerer")
  print("2. Barbarian")
  print("3. Warrior")
  print("4. Rogue")

  # get the player's choice
  choice = input("Enter the number of your choice: ")

  # determine the character class based on the player's choice
  if choice == "1":
    character_class = "Sorcerer"
    # start the sorcerer.py file
    exec(open("classes/sorcerer.py").read())
  elif choice == "2":
    character_class = "Barbarian"
    # start the barbarian.py file
    exec(open("classes/barbarian.py").read())
  elif choice == "3":
    character_class = "Warrior"
    # start the warrior.py file
    exec(open("classes/warrior.py").read())
  elif choice == "4":
    character_class = "Rogue"
    # start the rogue.py file
    exec(open("classes/rogue.py").read())
  else:
    character_class = "Unknown"
    print("Invalid choice. Please try again.")

  # save the character data to the char.data file
  with open("savedata/char.data", "w") as file:
    file.write(name + "," + character_class)

  # print the character class
  print("Your character class is: " + character_class)

elif choice == "3":
  # exit the game
  print("Thank you for playing Text Adventure by AI. Goodbye!")

else:
  # invalid choice
  print("Invalid choice. Please try again.")
