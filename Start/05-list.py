##### list #####

# 1 list()

my_list = list("abcde")

print(my_list)  # ['a', 'b', 'c', 'd', 'e']

# 2 []

my_list_2 = ["a", 18, "c", "d", "e", False]

print(my_list_2)  # ["a", 18, "c", "d", "e", False]

# 3 my_list[start:stop:step]

my_list_3 = [1, 2, 3, 4, 5]

print(my_list_3[0:3])  # [1, 2, 3]

print(my_list_3[0:3:2])  # [1, 3]

# 4 append()

my_list_4 = [1, 2, 3, 4, 5]

my_list_4.append(777)

print(my_list_4)  # [1, 2, 3, 4, 5, 777]

# 5 clear()

my_list_5 = [1, 2, 3, 4, 5]
my_list_5.clear()

print(my_list_5)  # []

# 6 extend()

first_list = [1, 2, 3]
second_list = [4, 5, 6]
first_list.extend(second_list)

print(first_list)  # [1, 2, 3, 4, 5, 6]

# 7 index()

my_list_7 = [1, 1, 2, 2, 3, 4, 5]

print(my_list_7.index(5))  # 6 (index from 0)

# 8 pop()

my_list_8 = [1, 2, 3, 4, 5, 6]

my_list_8.pop()
print(my_list_8)  # [1, 2, 3, 4, 5]

my_list_8.pop(0)
print(my_list_8)  # [2, 3, 4, 5]

# 9 reverse()

my_list_9 = [1, 2, 3, 4, 5, 6]
my_list_9.reverse()
print(my_list_9)  # [6, 5, 4, 3, 2, 1]

# 10 sort()

my_list_10 = [3, 1, 2, 6, 4, 5]
my_list_10.sort()
print(my_list_10)  # [1, 2, 3, 4, 5, 6]

my_list_10.sort(reverse=True)
print(my_list_10)  # [6, 5, 4, 3, 2, 1]

# 11 for element in my_list:

my_list_11 = [1, 2, 3, 4, 5, 6]

for element in my_list_11:
    print(element)  # 1 2 3 4 5 6

print("--------------------")

# task 1

task_1 = [1, 2, 3, 4, 5, 6]

for el in task_1:
    if el % 2 == 0:
        task_1.remove(el)

print(task_1)  # [1, 3, 5]

print("--------------------")

# task 2

task_2 = [1, 2, 3, 4, 5, 6, 7]
task_2_result = []

for el in task_2:
    task_2_result.append(el**2)

print(task_2_result)  # [1, 4, 9, 16, 25, 36]

print("--------------------")

# task 3 find a max number

task_3 = [1, 3, 2, 6, 5, 7, 4]
task_3.sort()
task_3_result = task_3.pop()

print(task_3_result)  # 6

# or
task_3 = [1, 3, 7, 2, 6, 5, 4]
task_3.sort(reverse=True)
print(task_3[0])  # 6

# or
max_element = task_3[0]
for element in task_3:
    if element > max_element:
        max_element = element
print(max_element)  # 6

print("--------------------")

# Print the number of items in the list:

my_list_11 = ["apple", "banana", "cherry"]
print(len(my_list_11))

print("--------------------")

# What is the data type of a list?

my_list_12 = ["apple", "banana", "cherry"]
print(type(my_list_12))


# Using the list() constructor to make a List:

# note the double round-brackets
my_list_13 = list(("apple", "banana", "cherry"))
print(my_list_13)
