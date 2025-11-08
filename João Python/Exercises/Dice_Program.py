#Exercise: Dice Rolling Game

import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"), 
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"), 
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"), 
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"), 
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")}

dice = []

total = 0

running = True
while running:
    while True:
        player_num = input("How many dice would you want to roll?: ")
        if not player_num.isdigit():
            print("That value isn't valid, pick again!")
        else:
            player_num = int(player_num)
            if player_num <= 0 or player_num >= 15:
              print("That number isn't valid, pick again!")
            else:
              break
        
    for die in range(player_num):
        dice.append(random.randint(1, 6))

    for line in range(5):
      for die in dice:
        print(dice_art.get(die)[line], end = "")
      print()
    
    for die in dice:
      total += die

    print(f"Your total is {total}")

    dice.clear()
    total = 0
    
    while True:
       play_again = input("Play again (y/n): ").lower()

       if play_again == "y":
         break
       elif not play_again == "n":
          print("That isn't an option")
       else:
          running = False
          break
    

print("Thanks for playing!")