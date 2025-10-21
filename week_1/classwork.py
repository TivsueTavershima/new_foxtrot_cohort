# ====================== PYTHON BEGINNER CLASSWORK ======================

# 1. Write 3 examples using comparison operators (==, !=, >, <, >=, <=).
#    Print the result for each one.


# No 1 answer here
stored_value = 5
search_value = 3

equal_to = 5 == 3
print("equal to:", search_value)

not_equal_to = 5 != 3
print("not equal to:", search_value)

less_than = 5 < 3
print("lees than:", search_value)

greater_than = 5 > 3
print("greater than:", search_value)

graeter_than_and_equal_to = 5 >= 3
print("greater than and equal to:", search_value)

less_than_and_equal_to = 5 <= 3
print("less than and equal to:", search_value)


# 2. Create two variables: stored_value = 12 and search_input = 12.
#    Check if they are equal and print the result.


# No 2 answer here
stored_value = 12
search_value = 12

equal_to = 12 == 12
print("equal to:", search_value)

# 3. Use comparison operators to check:
#    - if 5 is greater than 10
#    - if 15 is less than or equal to 20
#    Print both results.


# No 3 answer here

compare= 5 > 10
compare = 15 <= 20
print(compare,compare)

# 4. Use logical operators to check:
#    - if a person's age is greater than or equal to 18 AND if they have a driver's license.
#    Example:
#    age = 20
#    license = "yes"
#    Print the result of the comparison.


# No 4 answer here

age = 20
licence = "yes"

is_driver_licence = age >= 18 and licence
print(is_driver_licence)



# 5. Use OR (||) to check if one of these is true:
#    temperature = 35
#    raining = False
#    Check if temperature > 30 or raining == True
#    Print the result.

# No 5 answer here

temperature = 35
raining = 'false'

one_is_true = temperature or raining == True
print(one_is_true)

# 6. Use NOT to flip the value of a variable:
#    Example:
#    is_tired = False
#    Use NOT to make it True and print both values.

# No 6 answer here
are_you_okay = 'false'
negate_value = not are_you_okay
print("not",negate_value)

# 7. Create 4 string variables:
#    - One using single quotes
#    - One using double quotes
#    - One using triple single quotes
#    - One using triple double quotes
#    Print all of them.

# No 7 answer here
valuable1 = 'hello'
valuable2 = "hi"
valuable3 = '''how are you'''
valuable4 = """i'm fine"""
print(valuable1,valuable2,valuable3,valuable4)


# 8. Write a sentence that uses \n for a new line and \t for a tab space.
#    Print it and see how it looks.

# No 8 answer here

sentence = "hello sir, \n\thow are you"
print(sentence)


# 9. Use string methods:
#    - Make a string called name = " miracle "
#    - Remove spaces using .strip()
#    - Change it to uppercase using .upper()
#    - Change it to lowercase using .lower()
#    - Print each result.


# No 9 answer here

name = ' Miracle '
remove_space = name.strip()
print(name)

upper_case = name.upper()
print(upper_case)

lower_case = name.lower()
print(lower_case)





# 10. Do the following with strings:
#     - Concatenate two strings, for example: "Python" + " Programming"
#     - Use an f-string to print your name inside a sentence (Example: f"My name is {name}")
#     - Use * (multiplication) to repeat a word 3 times.
#     - Print all results.


# No 10 answer here
val = 'python'
val1 = 'programming'

concat = "python " + "programe"
print(concat)

print(f"my first test in {val} {val1}")

me = name * 3
print(me)

