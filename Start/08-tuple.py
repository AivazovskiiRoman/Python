##### Python Tuples #####
# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable

tuple_1 = (1, 2, 3)
print(tuple_1)  # (1, 2, 3)

# allow duplicates

tuple_1_1 = (1, 2, 3, 3, 3, 3)
print(tuple_1_1)  # (1, 2, 3, 3, 3, 3)

print("--------------------")

# a, b = b, a

tuple_2 = (1, 2)
x, y = tuple_2
print(x)  # 1
print(y)  # 2

x, y = y, x
print(x)  # 2
print(y)  # 1

print("--------------------")

# for element_1, element_2 in [(1,2), (2,4)]

tuple_3 = [(1, 2), (2, 3)]
for first, second in tuple_3:
    print(first, second)
# Output:
# 1 2
# 2 3

print("--------------------")

# Tuple Methods

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
