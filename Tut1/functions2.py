# import os   ...imports operating system
# os.listdir gives the list of files in the folder
# help(os) gives all the os module.
#  if you add "__file__" to it it gives you the path.
#  os.__file__ will give you the path.
"""
this is a doc string
import imp
imp.reload(fileYouWantToReload)
fileYouWantToReload.__doc__ will load the docstrings
you can access functions using dots
"""
def minutesToHours(minutes):
    """ This converts minutes to hours"""
    hours = minutes/60
    return hours
