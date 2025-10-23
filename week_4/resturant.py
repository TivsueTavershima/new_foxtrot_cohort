import time
foods = [
    {"name": "bread", "price": 1000},
    {"name": "milk", "price": 2000},
    {"name": "eggs", "price": 3000},
    {"name": "juice", "price": 1500},
 ]
def display_menu():
    print("welcome to the restuan")
for food in foods:
        print(f"name: {food['name']}, 'price:'{food['price']}")
        time.sleep(0.7)


def search_for_food(searched_food):
    for food in foods:
        if food['name'].lower().remove(" " "") == searched_food.lower().remove(" " ""):
            return food
        else:
            return False
        

def main():
    bill = 0
while True:
        display_menu()  
        options = input("what do you want to buy\n write the name of the food: ")
        is_food = search_for_food(options)
        if type(is_food) == dict:
         purchase = input(f"the price of this food is {is_food['price']}\ndo you want to buy? (yes/no): ")
        if purchase == 'yes':
         bill = bill + float(is_food["price"])
        option_two = input(f"your bill is  {bill}\ndo you want to buy more? (yes/no): ")
        if option_two == "yes":
         continue
        else:
          print(f"thank you for your purchased. Total bill is : {bill}")
          break
else:
       print()
         