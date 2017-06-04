from tkinter import *
from backend import *
import frontend as FE

window = Tk()

window.wm_title("Bookstore")

titleLabel = Label(window,text = 'Title:')
titleLabel.grid(row = 0, column = 0)

autherLabel = Label(window,text = 'Auther:')
autherLabel.grid(row = 0, column = 2)

yearLabel = Label(window,text = 'Year:')
yearLabel.grid(row = 1, column = 0)

ISBNLabel = Label(window,text = 'ISBN:')
ISBNLabel.grid(row = 1, column = 2)

titleInput = StringVar()
titleEntry = Entry(window, textvariable = titleInput)
titleEntry.grid(row = 0, column = 1)

autherInput = StringVar()
autherEntry = Entry(window, textvariable = autherInput)
autherEntry.grid(row = 0, column = 3)

yearInput = StringVar()
yearEntry = Entry(window, textvariable = yearInput)
yearEntry.grid(row = 1, column = 1)

ISBNInput = StringVar()
ISBNEntry = Entry(window, textvariable = ISBNInput)
ISBNEntry.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

list1.bind('<<ListboxSelect>>', FE.getSelectedRow) #this is to select something from a listbox

scroller = Scrollbar(window)
scroller.grid(row = 2,column = 2, rowspan = 6)

list1.configure(yscrollcommand = scroller.set)
scroller.configure(command = list1.yview)

viewAllBtn = Button(window, text = "View all", width = 12, command = FE.viewCommand)
viewAllBtn.grid(row = 2, column = 3)

searchBtn = Button(window, text = "Search Entry", width = 12, command = FE.searchCommand)
searchBtn.grid(row = 3, column = 3)

addBtn = Button(window, text = "Add Entry", width = 12, command = FE.addBook)
addBtn.grid(row =4, column = 3)

updateBtn = Button(window, text = "Update", width = 12, command = FE.updateRow)
updateBtn.grid(row = 5, column = 3)

deleteBtn = Button(window, text = "Delete", width = 12, command = FE.deleteItem)
deleteBtn.grid(row = 6, column = 3)

closeBtn = Button(window, text = "Close", width = 12, command = window.destroy)
closeBtn.grid(row = 7, column = 3)


window.mainloop()
