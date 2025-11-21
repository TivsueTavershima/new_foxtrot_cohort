import time

foods = [
    {"name": "Yam", "price": "1000"},
    {"name": "Rice and Beans", "price": "1500"},
    {"name": "Sphagetti", "price": "1200"},
    {"name": "Fufu", "price": "2500"},
]


def display_food():
    print(f"{"==" * 24}\nJust my food Menu\n{"==" * 24}")
    for food in foods:
        print(f"Name: {food['name']}, Price: {food['price']}\n{"--" * 24}")
        time.sleep(0.5)


def search_for_food(searched_food):
    for food in foods:
        if food["name"].lower().replace(" ", "") == searched_food.lower().replace(" ", ""):
            return food
    else:
        return False


def main():
    bill = 0
    while True:
            display_food()
            option = input("What do you want to buy?\n(Write the name of food): ")

            is_food = search_for_food(option)

            if type(is_food) == dict:
                purchase = input(f"The price of this food is {is_food["price"]}.y\nDo you want to buy it? (y/n):")

                if purchase == "y":
                    bill = bill + float(is_food["price"])

                    option_two = input(f"Your bill is {bill}. Do you want to buy more? (y/n)")
                    
                    if option_two == "y":
                        continue
                    else:
                        print(f"{"==" * 24}\nThank you for your purchase. Total bill: {bill}\n{"==" * 24}")
                        break
            else:
                print("Sorry we don't have the requested food.")
                time.sleep(4)

main() # Running the program