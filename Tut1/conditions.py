def celToFer(cel):
    if cel > (-273.15):
        fer = cel * (9/5) + 32
        return str(fer)
    else:
        return "not possible"

cel = float(input("2: type a degree in cel: "))
output = str(cel) + " = " + celToFer(cel)
print(output)
