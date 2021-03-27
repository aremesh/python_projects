import random


# Dice function requiring: min and max
def dice(min, max):
    """Minimal and Maximum dice count required"""
    value = random.randint(min, max)
    print(value)


running = True

while running:
    # Roll the dice
    dice(1, 6)
    # After dice number returned check if user wants to roll again
    roll_again = input("Roll the dices again? (Yes/No): ")
    if roll_again == "Yes":
        # Continu in the loop
        continue
    else:
        # Breaks the infinite loop
        running = False
