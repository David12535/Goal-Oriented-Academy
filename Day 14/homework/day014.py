#1

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(array1)
sum=0
while sum != 20:
    sum += 1
    print(sum)

#2 
array2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(array2)
sum=0
while sum != 20:
    sum += 2
    print(sum)

#3

my_list = []

for i in range(100, 201):
    my_list.append(i)

print(my_list[-10])

#4

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))


for num in range(num1, num2 +1):
    if num % 5 == 0:
        print (num)


#5

age = int(input("Enter your age: "))
array3 = ["David", "Akaki", "Saba"]

if age >= 18:
    name = input("please enter your name: ")
    array3.append(name)
    print(array3)

else:
    print("you are not old enough")