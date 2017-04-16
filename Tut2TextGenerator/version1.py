import string, random

inputLetter1 = input("Enter the first letter you want. Enter 'v' for vowels; 'c' for consonants and 'l' for any letter:")
inputLetter2 = input("Enter the second letter you want. Enter 'v' for vowels; 'c' for consonants and 'l' for any letter:")
inputLetter3 = input("Enter the third letter you want. Enter 'v' for vowels; 'c' for consonants and 'l' for any letter:")

inputArr = [inputLetter1, inputLetter2, inputLetter3]

def generator():
    alphabet = string.ascii_lowercase
    vowels = 'aeiouy'
    consonants = 'qwrtpsdfghjklzxvbnm'
    word = ""
    for i in inputArr:
        if i =='v':
            word += random.choice(vowels)
        elif i == 'c':
            word += random.choice(consonants)
        elif i == 'l':
            word += random.choice(alphabet)
        else:
            word += i
    return word

for i in range(10):
    print(generator())
