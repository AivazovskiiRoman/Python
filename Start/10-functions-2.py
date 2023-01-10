##### Python Functions, part 2 #####

# global
x = 1


def print_x():
    print(x)


print_x()  # 1
print(x)  # 1

print("--------------------")


# local
def print_local_y():
    y = 1
    print(y)


print_local_y()  # 1

# print(y)  # NameError: name 'y' is not defined


# but if we need to use a local var we can use
def get_z():
    z = 7
    return z


z_from_local = get_z()
print(z_from_local)  # 7

print("--------------------")


# function in function
def main():
    x = 10

    def internal():
        return 1

    internal_result = internal()
    return x + internal_result


m = main()
print(m)  # 11

print("--------------------")

##### Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function
# add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access
# the items accordingly:


def kids_func(*kids):
    print(kids)
    print("The youngest child is: " + kids[1])


kids_func("Roman", "Anna", "Ava")
# Output:
# ('Roman', 'Anna', 'Ava')
# The youngest child is: Anna

print("--------------------")


##### Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.


def keyword_func(child3, child2, child1):
    print("The youngest child is: " + child1)


keyword_func(child1="Anna", child2="Roman", child3="Theo")
# Output:
# The youngest child is: Anna

print("--------------------")

##### Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into
# your function, add two asterisk: ** before the parameter name in
# the function definition.

# This way the function will receive a dictionary of arguments, and
# can access the items accordingly:


def arbitrary_func(**kid):
    print("His last name is " + kid["lname"])


arbitrary_func(fname="Roman", lname="Himadinov")
# Output:
# His last name is Himadinov

print("--------------------")

##### Default Parameter Value
# If we call the function without argument, it uses the default value:


def default_func(country="USA"):
    print("I am from " + country)


default_func("Sweden")  # I am from Sweden
default_func()  # I am from USA
default_func("Brazil")  # I am from Brazil

print("--------------------")


##### Passing a List as an Argument
# You can send any data types of argument to a function (string, number,
# list, dictionary etc.), and it will be treated as the same data type
# inside the function.

# E.g. if you send a List as an argument, it will still be a List when
# it reaches the function:


def passing_a_list_func(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

passing_a_list_func(fruits)
# Output:
# apple
# banana
# cherry

print("--------------------")

##### The pass Statement
# function definitions cannot be empty, but if you for some reason have a
# function definition with no content, put in the pass statement to avoid
# getting an error.


def pass_func():
    pass


pass_func()

print("--------------------")


##### Recursion
# Python also accepts function recursion, which means a defined function
# can call itself.


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


tri_recursion(5)
# Output:
# 1
# 3
# 6
# 10
# 15

print("--------------------")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result_factorial = factorial(5)
print(result_factorial)  # 120


print("--------------------")

##### Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only
# have one expression.

# Syntax > lambda arguments : expression

lambda_a = lambda a: a + 10
print(lambda_a(5))  # 15


some_list = [1, 2, 5, 3, 4]
some_list.sort(key=lambda x: -x)
print(some_list)  # [5, 4, 3, 2, 1]

some_list.sort(key=lambda x: x)
print(some_list)  # [1, 2, 3, 4, 5]
