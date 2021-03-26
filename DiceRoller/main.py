import random

def dice(min, max):
    value = random.randint(min, max)
    print(value)

running = True

while running:
    dice(1, 6)
    roll_again = input("Roll the dices again? (Yes/No): ")
    if roll_again == "Yes":
        continue
    else:
        running = False