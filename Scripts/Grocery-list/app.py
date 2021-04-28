# imports


# Variables
grocery_list = {}


def add_grocery(food_type, item):
    if food_type in grocery_list.keys():
        grocery_list[food_type].append(item)
    else:
        grocery_list[food_type] = [item]

add_grocery('Fruit', 'Apple')
add_grocery('Fruit', 'Bannana')
add_grocery('Candy', 'Lolly\'s')


print("Things to buy:")
for key, items in grocery_list.items():
    print("\tProduct type:", key)
    for item in items:
        print("\t\t" , item)

# Improvements to de made.
# - Asking input key and name of product
# - Adding the input to the dict
# - On finisching write to a styled txt file
