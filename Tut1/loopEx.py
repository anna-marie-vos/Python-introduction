temp = [10,-20,-289,100]

def celToFer(cel):
    if cel > (-273.15):
        fer = cel * (9/5) + 32
        return str(fer)
    else:
        return "not possible"

for i in temp:
    print (celToFer(i))
