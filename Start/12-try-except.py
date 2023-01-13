##### Try Except
# The 'try' block lets you test a block of code for errors.

# The 'except' block lets you handle the error.

# The 'else' block lets you execute code when there is no error.

# The 'finally' block lets you execute code, regardless of the result
# of the try- and except blocks.

print("--------------------")

# 1 / 0
# Output: ZeroDivisionError: division by zero

print("--------------------")

try:
    1 / 0
except:
    print("You cannot divide by zero")

# Output: You cannot divide by zero

print("--------------------")

##### Base Exception

# try:
#   ...
# except BaseException:
#   ...

try:
    print(abc)
except NameError as error:
    print(error)

# Output: name 'abc' is not defined

print("--------------------")

##### Many Exceptions

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Output: Variable x is not defined

print("--------------------")

##### Else
# The else keyword is define a block of code to be executed if no errors
# were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Output:
# Hello
# Nothing went wrong

print("--------------------")

##### Finally
# The finally block, if specified, will be executed regardless if the try block
# raises an error or not.

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Output:
# Something went wrong
# The 'try except' is finished

print("--------------------")

# This can be useful to close objects and clean up resources:

try:
    f = open("file.txt")
    try:
        f.write("Some text")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# Output: Something went wrong when opening the file

print("--------------------")


##### Raise
# Raise an error and stop the program if some_var is lower than 0:
# some_var = -1

# if some_var < 0:
#     raise Exception("Sorry, no numbers below zero")

# Output:
# Traceback (most recent call last)
# Exception: Sorry, no numbers below zero


# some_var = "hello"

# if not type(some_var) is int:
#     raise TypeError("Only integers are allowed")

# Output:
# Traceback (most recent call last)
# TypeError: Only integers are allowed

print("--------------------")

# Task 1: show month name


def get_month(number):
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }

    try:
        return months[number]
    except KeyError as key_error:
        print(key_error, ", use only numbers from 1 to 12")
    except TypeError as type_error:
        print(type_error, ", use only numbers from 1 to 12")


print(get_month(1))  # Jan
print(get_month([1]))  # unhashable type: 'list' , use only numbers from 1 to 12
print(get_month("a"))  # 'a' , use only numbers from 1 to 12 > None
print(get_month(20))  # 20 , use only numbers from 1 to 12 > None
print(get_month(0))  # 0 , use only numbers from 1 to 12 > None

print("--------------------")


# Task 2: check for unique symbols


def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, "use only strings, lists or sets")


print(check_sequence_unique([1, 2, 3, 4]))  # True
print(check_sequence_unique([1, 2, 3, 4, 4, 4]))  # False
print(check_sequence_unique("abc"))  # True
print(check_sequence_unique("abccc"))  # False

print(check_sequence_unique(123))
# Output: 'int' object is not iterable use only strings, lists or sets. None
print(check_sequence_unique(True))
# Output: 'bool' object is not iterable use only strings, lists or sets. None
