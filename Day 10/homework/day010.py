#პირველი დავალება
for i in range(21):
    print(i)

#მეორე დავალება
sum=0
for i in range(50,101):
    sum += i
print(sum)  

#მესამე დავალება
for i in range (-10, 10, 3):
    print(i)  

#მეოთხე დავალება
num1=int(input("enter your first number: "))
num2=int(input("enter your second number: "))

if num1 > num2:
    for i in range(num2 , num1, 2):
        print(i)
elif num2 > num1:
    for i in range(num1 , num2 , 2):
        print(i)
else:
    print(f"{num1}={num2}")      

#მეხუთე დავალება       
num3=int(input("enter your first number: "))
num4=int(input("enter your second number: "))
sum = 0
if num3 > num4:
    for i in range(num4 , num3 + 1):
        sum += i  
elif num4 > num3:
    for i in range(num3 , num4 + 1):
        sum += i 
else:
    print(f"{num3}={num4}")     
print(sum)