##### loops #####

##### while #####

counter = 0
while counter < 5:
    counter += 1
    print("counter = ", counter)

print("total = ", counter)

print("--------------------")

# else Print a message once the condition is false:

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print("--------------------")

# Else in For Loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("--------------------")

##### for #####

for number in range(1, 6):
    print(number)


print("--------------------")

for number in range(1, 6):
    if number == 3:
        break
    print(number)

print("--------------------")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

print("--------------------")

# task 1

for number in range(0, 101):
    if number % 2 == 0:
        print(number)

print("--------------------")

# task 2
word = ""

for string in "hello":
    if string == "l":
        string = "s"
    word += string

print(word)

print("--------------------")

# task 3
back_counter = 99

while back_counter > 0:
    if back_counter % 5 == 0:
        print(back_counter)
        break
    back_counter -= 1
