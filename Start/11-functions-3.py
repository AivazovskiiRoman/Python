##### Python Functions, part 3 #####

print("hello")  # hello


len_x = len("hello")
print(len_x)  # 5


str = str(777)
print(str)  # '777'
print(type(str))  # <class 'str'>


int = int(777)
print(int)  # 777
print(type(int))  # <class 'int'>


float = float(777)
print(float)  # 777.0


list = list("777")
print(list)  # ['7', '7', '7']


dict = dict([("key", "value")])
print(dict)  # {'key': 'value'}


set = set([1, 2, 3, 4, 5, 5, 5, 5, 5, 5])
print(set)  # {1, 2, 3, 4, 5}


tuple = tuple("777")
print(tuple)  # ('7', '7', '7')


bool_1 = bool(1)
bool_2 = bool(0)
print(bool_1)  # True (-1 is true as well)
print(bool_2)  # False


sum_x = sum([7, 7, 7])
print(sum_x)  # 21


min = min([1, 2, 3])
print(min)  # 1


max = max([1, 2, 3])
print(max)  # 3


x = [1, 2, 3, 4, 5]
avg = sum(x) / len(x)
print(avg)  # 3.0


# Task 1
def numbers(n):
    for number in range(1, n + 1):
        print(number)


numbers(5)
# Output:
# 1
# 2
# 3
# 4
# 5


# Task 2
def rectangle(height, length):
    return height * length


h1 = 10
l1 = 45
area1 = rectangle(h1, l1)
print(area1)  # 450
