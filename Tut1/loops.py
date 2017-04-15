emails = ["me@gmail.com","you@hotmail.com","them@gmail.com"]

for email in emails:
    if "gmail" in email:
        print (email)

for i in (1,2,3):
    print(i+1)

a = "Tricky"
for i in a[:3]:
    print(i)

lst = ["Terribly Tricky"]
for word in lst:
    for letter in word[-6:]:
        print (letter)

names=['james','jock','gem']
emails = ['gmail','hotmail','yhoo']

for i,j in zip(names,emails):
    print(i,j)
