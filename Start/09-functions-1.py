##### Python Functions, part 1 #####
# In Python a function is defined using the def keyword


def my_function():
    print("Run a function")


my_function()  # Run a function

print("--------------------")

# Arguments (Parameters)


def show_message(msg):
    print(msg)


show_message("Some message")  # Some message
show_message("Another message")  # Another message

print("--------------------")


# Return values


def sum(a, b):
    return a + b


result = sum(7, 3)
print(result)  # 10
print(sum(5, 2))  # 7
