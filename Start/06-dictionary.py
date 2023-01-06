##### dictionary #####
# Dictionaries are used to store data values in key:value pairs.

my_dict = {"key": "value", 7: True, 0.1: "Some value"}
print(my_dict)
print(my_dict["key"])  # value
print(my_dict[7])  # True
# error: print(my_dict["Maybe"])  # KeyError: 'Maybe'

print("--------------------")

# .get(key)

print(my_dict.get("key"))  # value
print(my_dict.get(7))  # True
print(my_dict.get("Maybe"))  # None
# or
print(my_dict.get("Maybe"), "Some message")  # None Some message

print("--------------------")

# .cler()
my_dict2 = {"key": "value", 7: True, 0.1: "Some value"}
my_dict2.clear()
print(my_dict2)  # {}

print("--------------------")

# .items()
print(my_dict.items())
# dict_items([('key', 'value'), (7, True), (0.1, 'Some value')])

print("--------------------")

# pop(key)
my_dict3 = {"key": "value", 7: True, 0.1: "Some value"}
print(my_dict3.pop(7))  # True
print(my_dict3)  # {'key': 'value', 0.1: 'Some value'}

print("--------------------")

# popitem()
print(my_dict3.popitem())  # (0.1, 'Some value')
print(my_dict3)  # {'key': 'value'}

print("--------------------")

# update()
d = {1: "a", 2: "b", 3: "c"}
d2 = {4: "d", 5: "e", 6: "f"}

d.update(d2)
print(d)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

d.update({1: "z"})
print(d)  # {1: 'z', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

d.update({7: "r"})
print(d)  # {1: 'z', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'r'}

print("--------------------")

# values()
print(d.values())  # dict_values(['z', 'b', 'c', 'd', 'e', 'f', 'r'])

# keys()
print(d.keys())  # dict_values(['z', 'b', 'c', 'd', 'e', 'f', 'r'])

print("--------------------")

# len()
# To determine how many items a dictionary has, use the len() function
my_dict4 = {1: "boo", 2: "some", 3: "test"}
print(len(my_dict4))  # 3

# type()
print(type(my_dict4))  # <class 'dict'>

print("--------------------")

# the dict() constructor
my_dict5 = dict(name="John", age=26, country="USA")
print(my_dict5)

print("--------------------")

# task 1
my_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9, 10, 10]
value_to_count = 3
count_dict = {value_to_count: 0}

for element in my_list:
    if element == value_to_count:
        count_dict[value_to_count] += 1

print(count_dict)  # {3: 3} we have 3 elements "3" in the list

print("--------------------")


# task 1 updated
count_dict_2 = {}

for element in my_list:
    if element in count_dict_2:
        count_dict_2[element] += 1
    else:
        count_dict_2[element] = 1

print(count_dict_2)
# {1: 2, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3, 8: 1, 9: 1, 10: 2}

print("--------------------")

for key, value in count_dict_2.items():
    print("Key:", key, "Count:", value)

# Key: 1 Count: 2
# Key: 2 Count: 2
# Key: 3 Count: 3
# Key: 4 Count: 1
# Key: 5 Count: 1
# Key: 6 Count: 2
# Key: 7 Count: 3
# Key: 8 Count: 1
# Key: 9 Count: 1
# Key: 10 Count: 2

print("--------------------")

# task 2
task_2 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
for key, value in task_2.items():
    if key % 2 == 0:
        print(key, value)
# Output
# 2 2
# 4 4

print("--------------------")

# task 3
task_3 = {"aurora": 25, "angela": 28, "james": 33, "mark": 48}
new_task_3 = {}

for name, age in task_3.items():
    if name[0] != "a":
        new_task_3[name] = age

print(new_task_3)  # {'james': 33, 'mark': 48}

print("--------------------")
