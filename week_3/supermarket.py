items = ["Fanta", "Bread", "Milk", "Pillow", "Pan"]
sales = [
    {"name": "King", "item": "Bread"},
    {"name": "Peter", "item": "Milk"}
]

print(f"{"==" * 24}\nWelcome to Moku Supermarket\n{"==" * 24}")
name = input("Please tell us your name: ")
user_item = input(
    f"Hello {name}. \nWhat do you want to buy?\nWe have {items}\nWrite the name of what you want:").upper()
print("")

if user_item in items:
    option = input(
        f"You selected{user_item}. Do you want to buy?\n(Chose Y/N):")
    if option == "Y":
        sales.append({"name": name, "item": user_item})
        print("Thank you. Have a nice day")
    elif option == "N":
        print("I'm sorry. Have a nice day ")
    else:
        print("You choose the wrong option")
else:
    print("Sorry, we don't have that in store")


print(sales)
