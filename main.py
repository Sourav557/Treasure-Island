print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at crossroad, where do you want to go ? Type "left" or "right".').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There ia an Island in tje middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors one red, one yellow, one blue which colour do you choose ?").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game over.")
    elif choice3 == "yellow":
      print("You found the treasure ! You won")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game over")
    else:
      print("You choose a door that doesn't exit. Game over")
  else:
    print("You got attacked by trout. Game over")
else:
  print("You fell into a hole. Game over")