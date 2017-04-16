import string, random

def generator():
    alphabet = string.ascii_lowercase
    letter1 = random.choice(alphabet)
    letter2 = random.choice(alphabet)
    letter3 = random.choice(alphabet)
    name = letter1 + letter2 + letter3
    return (name)

print(generator())
