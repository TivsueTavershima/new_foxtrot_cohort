#LOOP 
# loop is a block of code that keeps on running until a conditon is met.

# Types of loops
#1. for loop
#2. while loop

num = 0
while num < 10:
    print(num)
    num = num + 1

people = ["john", "joe", "jane", "mary", "paul"]

search_name = input("who are you looking for: ")
for person in people:
    if person == search_name:
        people.remove(person)
        print(f"{search_name} has been removed")
        break # stop the loop
else:
        print("the person you are looking for is not found")

numbers = [1,2,3,4,5,6,7,8,9,10]
updated_num = []
for num in numbers:
    num = num * 2
    updated_num.append(num)
else:
    print("NUMBERS:", numbers)
    print("UPDATED NUMBERS:", updated_num)

    first_num = [1,2,3,4,5]
    second_num = [6,7,8,9,10]

    for num in second_num:
         first_num.append(num)
    print(first_num)

people = ["john", "doe", "jane", "mary", "paul"]
email_user = []

for person in people:
     #concatenate
     email_address = person + "email.com"

     email_user.append(email_address)
else:
     print(email_user)

