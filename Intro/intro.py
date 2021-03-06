#! /usr/bin/env python3

# for loops
x = 5
for i in range(x):
    variable = i * x
    print(variable)

# if / elif / else
if x > 6:
    print('great')
elif x < 2:
    print('small')
else:
    print('your number is between 2 and 6')

# while
while x != 0:
    print(x)
    x -= 1

# because 0 is always false and any other number is true
# you an also write the while like this, but line 18 is better:
y = 7
while y:
    print('this is y: ',y)
    y -= 1

# infinate while loops can be exit by ctrl+c
# python does not have a do while. It uses break
while True:
    response = input()
    if int(response) % 7 == 0:
        print("you've devided by 7")
        break

# functions work with def
def square(x):
    return x * x

print('this is a function',square(5))
