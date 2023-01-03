##### ternary operator #####


answer = "Hello" if 1 == 2 else "Goodby"
print(answer)
answer = "Hello" if 1 == 1 else "Goodby"
print(answer)

myVariable = 3
print(myVariable)

my_variable = 5
print(my_variable)

# task
price = 1501

if price > 1000:
    print("Your discount is 10%")
    price *= 0.9
elif price > 500:
    print("Your discount is 5%")
    price *= 0.95
elif price > 100:
    print("Your discount is 3%")
    price *= 0.97
else:
    print("Sorry, no discount for you")

print(price)

# task
string = "Bo"
result = None if string == "" else string
print(result)

# optimization
result = None if not string else string
print(result)


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
    pass
