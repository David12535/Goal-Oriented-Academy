#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 77
b = 77
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#ExampleGet your own Python Server
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Booleans represent one of two values: True or False.
#In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

