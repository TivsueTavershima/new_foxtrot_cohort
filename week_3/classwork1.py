people = ["john", "joe", "jane", "mary", "paul"]
search_name = input("Remove name: ")

for person in people:
    if person == search_name:
       people.remove(person)
       print(f"{search_name} has been removed")
else:
    print("the person you are looking for is not found")