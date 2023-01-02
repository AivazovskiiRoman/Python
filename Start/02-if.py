##### if #####

counter = 0
if counter < 10:
    counter += 1
else:
    print(counter)

animal = "dog"
if animal == "cat":
    print("This is a cat")
elif animal == "dog":
    print("This is a dog")
else:
    print("I don't know this animal")


# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# and

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# if not

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
