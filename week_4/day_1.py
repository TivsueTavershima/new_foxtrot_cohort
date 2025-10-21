# FUNCTION is is block of code that performs a specific task.

# chaacteristics of functions
# 1. Modularity - functions allow you to break your code into smaller, manageable pieces.
# 2 . reuseabilty - once a function is defined, it can be called multiple times throughout your code.
# 3. readapility - functions make your code more organized and easier to read.


def addition():
    num_1 = 1
    num_2 = 2
    sum = num_1 + num_2
    return sum

output = addition # calling the function. 

def subtraction():
    return 2 - 1

output - subtraction()
print(output)

'''
what can a function return?
string 
boolean

'''
age = 21 # global variable
def fun():
    name = "king" # local variable
    return "his name is" + name + "and he is " + str(age)
print(
    fun()
)

# parameters and arguments
def fun_1(words): #parameters
    return words

print(
    fun_1("this is a parameter") # arguments
)
def reusable_additon(num_one, num_two):
    return num_one + num_two

output_one = reusable_additon(14, 2)
output_two = reusable_additon(4, 4)
output_three = reusable_additon(16, 18)

#print(out_one, output_two, output_three)

# types of arguments
# 1. positional arguments

def func_2(pos1, pos2, pos3):
    return pos1 + pos2 + pos3

func_2("first valus", "second value", "third value") # positional arguments

func_2(pos1="first", pos2="second", pos3="third") # keyword arguments

# Defualt Arguments
def game(mode="easy"):
    return f"game on!!! mode {mode}"
