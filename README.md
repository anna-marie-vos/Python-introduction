# Python-introduction
* python is all about readability. so 4 x whitespaces are the standard.

## Python Installation
* it's already installed to check the version type: python3 --version
* or: python --version
* to find out which python to use type(in the terminal, this will output '/usr/bin/python3'): which python3

### terminal inline coding
* to run a python file in the terminall type: python fileName.py
* to test some code in the terminal type: python3
* to exit type: ctrl+D
* python doesn't really use {} to show end of functions it uses blank spaces. spacing is super inportant.
* a for loop looks like this:
* for i in range(5):
* (4 x spacebar)     x = i * 10
* (4 x spacebar)     print(x)
* an extra empty line shows that the function / code block is complete
* need help on a module? type: help(module_name)
* to exit help type: Q

### Import modules in terminal
* import modules: import module_name
* it import specific function from a module: from module_name import function_name
* example: from math inport factoral
* to rename a function during import: from math import factorial as fac
* to import multiple functions from a module: from module_name import (function_name,function_name2)
* to import everything from a module: from words import *

### Making exportable modules/scripts from functions:
* if __name__ == '__main__': fetch_words()

## advanced command line arguments parsing go to:
* python Standard Library: argparse
* of docopt
* checkout sys.argv[1]

## docstrings
* use """words words words""" in your code.
* this lets you add help file comments in the commandline
* in REPL import the module and then type: help(module_name)
* this will show all the usefull information on all the functions. Pretty cool

## to execute in terminal
* in your file make sure you've got "#! /usr/bin/env python3" on the top of your file
* write in the terminal: chmod +x fileName.py
* and then write in the terminal: ./fileName.py inputHere
* and that will also run the file in the terminal

## To run a simple server
* In the terminal type: python -m SimpleHTTPServer 3000
* this will run the local server to port 3000

### Webpages to take note of:
* http://www.tutorialspoint.com/python/

### Data types:
* list are the same as arrays. They are defined as: list = ['item1','item2']
* to retrieve items from a list: list[0] or list[1] this will retrieve 'item1' and 'item2' respectively
* tuples are immutible lists and are defined as list =('item1', 'item2') items are retrieved the same way as lists
* directory = object
* dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
