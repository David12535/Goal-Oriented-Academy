#Write a program that takes asks user for number (use input). If number is even, print that number is even. Else print that number is not even,
# also print next even number, for example if input is 15, print 16.
num1 = int(input("Please enter an int: "))

if num1 % 2 == 0:
    print("Number is even!")

else:
    print("Number is odd!")
    print("Next closest even number is" + " "  + str(num1 + 1))



#Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". 
#Also print the count of incorrect passwords.
correct_password = "Best Goa"
incorrect_tries = 0

while True:
        num1 = input("Please enter your password: ")
        if num1 == correct_password:
            print("Access granted!")
            break
        else:
            incorrect_tries += 1
            print("Password is incorrect! Please try again: ")
            print("You have " + str(incorrect_tries) + " tries")

#Write a function that takes a string as input and returns True if first character of that string is "G".
correct_letter = ['G', 'g']         
while True:
    user_input1 = str(input("Please input valid string: "))
    if user_input1[0] in correct_letter:
        print("Your string is correct!")
        break

    else:
        print("Please try again.")

#Ask user for five names (use input five times). Add all of them in one list and print only first three names.
name1 = str(input("Please input a valid string: "))

name2 = str(input("Please input a valid string: "))

name3 = str(input("Please input a valid string: "))

name4 = str(input("Please input a valid string: "))

name5 = str(input("Please input a valid string: "))

name_list = [name1, name2, name3, name4, name5]

print(name_list[0:3])       

#Write a function that checks if a given number is prime or not (prime number has only two divisors - გამყოფი) Use a for loop for this task.


#Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე).
list = []

for i in range(0, 11):
    list.append(i)

print(list) 

#Implement a simple calculator that takes two numbers and an operator (+, -, *, /) as input from the user and performs the corresponding
#operation. Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.
user_number = int(input("Please enter the first int: "))
user_number1 = int(input("Please enter the second int: "))

user_operator = input("Please enter an operator (+, -, *, /, **) ")

if user_operator == '+' :
    print(user_number + user_number1)

if user_operator == '-' :
    print(user_number - user_number1)

if user_operator == '/' :
    print(user_number / user_number1)

if user_operator == '*' :
    print(user_number * user_number1)

if user_operator == '**' :
    print(user_number ** user_number1)

#Ask user to enter name and print the last character of that string.
user_name = str(input("Please input a string: "))
while True:

        if len(user_name) > 0:
            (last_character) = user_name[-1]
            print (str(last_character))
            break

        else:
            print("Please input a correct variable! ")
#Using for loop, ask user for number. Then create a list which will have even numbers in next range: from 0 to user's number.
# At last, print out whole list. 
num1 = int(input("Please enter int: "))

my_list = []
for i in range(0, num1 + 1, 2):
    my_list.append(i)

print(my_list)

#Ask user for whole number. Then create a factorial for this number and print it out (If you don't know what a factorial is, google it). 
num1 = int(input("Please enter a whole number: "))

if num1 >= 0:
    factorial_result = 1


    for i in range(1, num1 + 1):
        factorial_result *= i


print(factorial_result)

