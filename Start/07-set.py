##### Python Sets #####
# Sets are used to store multiple items in a single variable

my_set_1 = {1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5}
print(my_set_1)  # {1, 2, 3, 4, 5}

print("--------------------")

# clear()

my_set_2 = {1, 2, 3, 4, 5}
my_set_2.clear()
print(my_set_2)  # set()

print("--------------------")

# pop()

my_set_3 = {1, 2, 3, 4, 5}
my_set_3.pop()
print(my_set_3)  # {2, 3, 4, 5}
my_set_3.pop()
print(my_set_3)  # {3, 4, 5}

print("--------------------")

# discard(element)

my_set_4 = {1, 2, 3, 4, 5}
my_set_4.discard(2)
print(my_set_4)  # {1, 3, 4, 5}

my_set_4.discard(6)  # the element has not found - do nothing

print("--------------------")

# remove(element)

my_set_5 = {1, 2, 3, 4, 5}
my_set_5.remove(2)
print(my_set_5)  # {1, 3, 4, 5}

# my_set_5.remove(6)  # the element has not found - KeyError: 6

print("--------------------")

# add(element)

my_set_6 = {1, 2, 3, 4, 5}
my_set_6.add(100)
print(my_set_6)  # {1, 2, 3, 4, 5, 100}

print("--------------------")

# union(element)

my_set_7 = {1, 2, 3, 4, 5}
my_set_7_2 = {1, 2, 3, 4, 5, 6, 7}
print(my_set_7.union(my_set_7_2))  # {1, 2, 3, 4, 5, 6, 7}

print("--------------------")

# intersection(element)

my_set_8 = {1, 2, 3}
my_set_8_2 = {3, 4}
print(my_set_8.intersection(my_set_8_2))  # {3}

print("--------------------")

# difference(element)

my_set_9 = {1, 2, 3}
my_set_9_2 = {3, 4}
print(my_set_9.difference(my_set_9_2))  # {1, 2}

print("--------------------")

# element in set_name

my_set_10 = {1, 2, 3}
print(2 in my_set_10)  # True
print(5 in my_set_10)  # False

print("--------------------")

# True and 1 is considered the same value

my_set_11 = {"aaa", "bbb", "ccc", True, 1, 2}
print(my_set_11)  # {True, 2, 'ccc', 'bbb', 'aaa'}

print("--------------------")

# intersection_update(element)

my_set_12 = {"aaa", "bbb", "ccc"}
my_set_12_2 = {"ggg", "mmm", "aaa"}
my_set_12.intersection_update(my_set_12_2)
print(my_set_12)  # {'aaa'}

print("--------------------")

# symmetric_difference_update(element)

my_set_13 = {"aaa", "bbb", "ccc"}
my_set_13_2 = {"ggg", "mmm", "aaa"}
my_set_13.symmetric_difference_update(my_set_13_2)
print(my_set_13)  # {'bbb', 'ccc', 'ggg', 'mmm'}

print("--------------------")

# Set Methods

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
