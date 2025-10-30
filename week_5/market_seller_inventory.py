
goods =[ 
        {'name': 'phone','price':50000,'category':'gadget','quantity':12,'date':'28-10-2025'},
        {'name': 'rice','price':7000,'category':'food','quantity':7,'date':'28-10-2025'},
        {'name': 'book','price':2000,'category':'confectionary','quantity':10,'date':'28-10-2025'},       
]


def list_input():
        name = input("Enter the name of the good: ")
        price = input(float("Enter the price: "))
        category = input('Enter the category: ')
        quantity = input(int("Enter the quantity: "))
        date_of_arrival = input("Enter the date (dd-mm-yyyy): ")
        
        print('')
        
        goods.append({
                "name":name,
                "price":price,
                "category":category,
                "quantity":quantity,
                "date_of_arrival":date_of_arrival
                
        })
        print(name + "option added successfully")
        
def display_goods():
        for good in goods:
           print("Name:", good["name"],
              " Price: " + str(good["price"]),
               " Category:", good["category"],
               " Date:", good["date_of_arrival"],
               " Quantity:", good["quantity"])

              
              
             
              
          
def add():
       total = sum(good["quantity"]for good in goods)
       print("total number of inventory",total)
       
       
def search_input():
    print(f"{10 * '='}\nSearch Result\n{10 * '='}")
search = input(f"Enter name or category to search\n: ").lower().strip()

found = False
for good in goods:
        if search in good["name"].lower() or search in good["category"].lower():
            print("Name:", good["name"],
                  "price:", good["price"],
                  "category: ₦" + str(good["category"]),
                  "quantity:", good["quantity"],
                  "date:", good["date"])
            found = True
if not found:
        print("No matching goods found.")


def main():
    print(f"{"==" * 12}\nMarket Seller Inventory.\n{"==" * 12}")
    while True:
        print(f"1. Add Goods \n2. View Inventory\n3. Calculate Total Number of Goods \n4. Search by Name or Category \n5. Exit")
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            display_goods()
        elif choice == "2":
            display_goods()
        elif choice == "3":
            add()
        elif choice == "4":
            search_input()
        elif choice == "5":
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.\n")

main()