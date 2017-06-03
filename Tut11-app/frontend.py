from tkinter import *
import backend as BE
import interface as interface

def viewCommand():
    for row in BE.view():
        interface.list1.insert(END, row)
