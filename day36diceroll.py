# dice roll simple program
import random

def roll_dice():
    return random.randint(1,6)

while True:
    user_input=input("Press Enter to roll or 'q' to quit:")
    if user_input=="q":
        break
    else:
        dice_roll=roll_dice()
        print("Rolling dice is:",dice_roll)