greetings = input("type your normal greeting: ")
print(greetings)

# input produces strings so it needs to be converted
age = input("what is your age: ")
NewAge = int(age) + 20
print(NewAge)

# in the python interactive area, you can find all the various methods
# then type dir("") for strings or if
# you have a variable add the variable name there and you can see all the standard methods.
# then to use it type "".length or whatever you want to use.
# you can also type help("".length) and it will give you more detail regarding it
# type \q to exit help
print("Python is fun"[-3:0])
print("Python is fun"[-3:-1])
print("Python is fun"[-3:])
print("Python is fun"[-3:][-1])
