meals_special = [10,30,40,20,80,25]  # --> unorderd form = [10,20,25,30,40,80]
''' burger= 10
    ice_cream = 30
    Drinks = 40 
    Beverages = 20
    Fish Burger = 80
    Chick_Burger = 25 '''


n = len(meals_special)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if meals_special[j]['popularity'] < meals_special[j + 1]['popularity']:
            meals_special[j], meals_special[j + 1] = meals_special[j + 1],meals_special[j]

    