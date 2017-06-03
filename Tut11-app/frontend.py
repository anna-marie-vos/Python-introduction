from tkinter import *
import backend as BE
import interface as interface

def viewCommand():
    interface.list1.delete(0,END)
    for row in BE.view():
        interface.list1.insert(END, row)

def searchCommand():
    interface.list1.delete(0,END)
    for row in BE.search(interface.titleInput.get(),
    interface.autherInput.get(), interface.yearInput.get(),
    interface.ISBNInput.get()):
        interface.list1.insert(END,row)

def addBook():
    BE.insert(interface.titleInput.get(),
    interface.autherInput.get(), interface.yearInput.get(),
    interface.ISBNInput.get())
    newEntry = (interface.titleInput.get(),
    interface.autherInput.get(), interface.yearInput.get(),
    interface.ISBNInput.get())
    interface.list1.insert(END, newEntry)

def getSelectedRow(event):
    global selectedRow #makes it a global variable
    index = interface.list1.curselection()[0]
    selectedRow = interface.list1.get(index)
    interface.titleEntry.delete(0,END)
    interface.autherEntry.delete(0,END)
    interface.yearEntry.delete(0,END)
    interface.ISBNEntry.delete(0,END)
    interface.titleEntry.insert(END, selectedRow[1])
    interface.autherEntry.insert(END, selectedRow[2])
    interface.yearEntry.insert(END, selectedRow[3])
    interface.ISBNEntry.insert(END, selectedRow[4])


def deleteItem():
    id = selectedRow[0]
    BE.delete(id)
    viewCommand()
