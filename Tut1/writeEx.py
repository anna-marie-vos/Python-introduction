temp = [10,-20,-289,100]

def celToFer(cel):
    if cel > (-273.15):
        fer = cel * (9/5) + 32
        return (str(fer)+"\n")
    else:
        return ""

with open("writeOutput.txt","w+") as File:
    for i in temp:
        File.write(celToFer(i))
