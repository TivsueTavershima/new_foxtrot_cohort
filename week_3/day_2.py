# LOOP  is a block of code that keeps on running till a condition is meet.

# Loops in Python are used to repeat actions efficiently.

# The main types are For loops (counting through items) and While loops (based on conditions).

# While Loop
# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false,
# the line immediately after the loop in the program is executed.

# NB: multiple line comment is used for block of codes for easy debugging.


num = 0
while num < 10:
 print(num)
num = num + 1


# Infinite While Loop
# If we want a block of code to execute infinite number of times
# then we can use the while loop in Python to do so.


while (True):
 print("Hello World!")


#     For Loop
# For loops is used to iterate over a sequence such as a list, tuple, string or range.
# It allow to execute a block of code repeatedly, once for each item in the sequence.
# The break statement in Python brings control out of the loop.

 numbers = [1,2,3,4,5,6,7,8,9,10]
 updated_num = []

 for num in numbers:
    num = num * 2
    updated_num.append(num)
 else:
    print("NUMBERS:", numbers)
    print("UPDATED NUMBERS:",updated_num)


 first_num = [1,2,3,4,5]
 second_num = [6,7,8,9,10]

 for num in second_num:
    first_num.append(num)
 else:
    print(first_num)

 people = ["John", "Peter", "Ade", "Oluadamilare", "king"]
 email_users = []

 for person in people:
    # Concatenation
    email_address = person + "@mail.com"

    email_users.append(email_address)
 else:
    print(email_users)


 name = input("Who are you looking for?: ").strip()

 for person in people:
    if name.lower() == person.lower():
        print(name)
        people.remove(person)
        print(f"{person} removed.")
        break
 else:
    print("This person is not in the list")