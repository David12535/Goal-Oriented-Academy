#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
#A variable created inside a function is available inside that function:

def myfunc():
  x = 120
  print(x)

myfunc()
 
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application. 
#To create a module just save the code you want in a file with the file extension .py:
#Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)

#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
#Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)

#Find the factorial of a number:
#Import math Library
import math
#Return factorial of a number
print(math.factorial(2))
print(math.factorial(4))
print(math.factorial(18))




