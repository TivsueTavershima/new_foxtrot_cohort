#  HIGHER ORDER FUNCTIONS
# higher ordre function are function that take other functions as arguments, or return a function.

def speak():
    return "ola. my name is taver."

def man(name, func):
    return f"{name}: {func()}"

call = man("jerry",speak)
print(call)

# map higher order function that return back a new list.

numbers = [1,2,3,4,5,6,7,8,9]

def multiply_by_2(item):
    return item * 2

map_func = map(multiply_by_2,numbers)
print(list(map_func))

# Filter: return a new filter list
def no_remainder(item):
    print(item)
    return item % 2 == 0 # Modulos - returns remainders when you divide

filter_func = filter(no_remainder,numbers)
print(list(filter_func))

