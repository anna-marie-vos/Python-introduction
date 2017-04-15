def minutesToHours(minutes):
    hours = minutes/60
    return hours

minutes = input("1: minutes to convert: ")
print(minutesToHours(int(minutes)))

# exercise 1: convert celcius to ferenheit
def celciusToFer(cel):
    fer = cel * (9/5) + 32
    return fer

cel = input("2: type a degree in cel: ")
output = cel + " = " +str(celciusToFer(float(cel)))
print(output)

#  exercise 2:
money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
output2 = money["under_bed"][1]
print(output2)
