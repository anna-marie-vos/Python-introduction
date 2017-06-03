from tkinter import *

window = Tk()

def convertKgs():
    kgs = float(kgInput.get())
    grams = kgs*1000
    pounds = kgs * 2.2046226218
    ounces = pounds * 16
    gramsOutput.insert(END,grams)
    poundsOutput.insert(END,pounds)
    ouncesOutput.insert(END,ounces)



instructions = Label(window,
    text = "Convert kg to grams, pounds and ounces")
instructions.grid(row = 0, column = 0)

kgLabel = Label(window,
    text = "Insert the kg you wish to convert:")
kgLabel.grid(row = 1, column = 0)

kgInput = StringVar()
kg = Entry(window, textvariable = kgInput)
kg.grid(row = 1, column = 1)

enterButton = Button(window, text="Convert", command = convertKgs)
enterButton.grid(row = 1, column = 2)

gramsLabel = Label(window, text = "Grams:")
gramsLabel.grid(row = 2, column = 0)
poundsLabel = Label(window, text = "Pounds:")
poundsLabel.grid(row = 3, column = 0)
ouncesLabel = Label(window, text = "Ouces:")
ouncesLabel.grid(row = 4, column = 0)

gramsOutput = Text(window, height = 2, width = 20)
gramsOutput.grid(row = 2, column = 1)
poundsOutput = Text(window, height = 2, width = 20)
poundsOutput.grid(row = 3, column = 1)
ouncesOutput = Text(window, height = 2, width = 20)
ouncesOutput.grid(row = 4, column = 1)


window.mainloop()
