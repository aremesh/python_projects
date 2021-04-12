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


print(grocery_list)
