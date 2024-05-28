name = "David"

print(10>5) #მეტია
print(10<5) #ნაკლებია
print(10 == 10) #ტოლია

print(6 >= 5) #ურდრის ან მეტია
print(5 <= 5) #უდრის ან ნაკლებია
print(3 >= 5) #უდრის ან მეტია

print(5 != 7) #არ უდრის

num = 32
print(32 + "hibuy") #int
print (32 + str("hibuy"))#სტრინგად ქცეული



#არასწორი ვერსია
num1 = input("please enter first number: ")
num2 = input("please enter second number: ")

print(num1 + num2)

#სწორი ვერსია
num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))

print(type(num1))

print(10/3)#ზუსტი განაყოფი
print(10//3)#რამდენჯერ მოთავსდება გამყოფში განაყოფი
print(10 % 3)#რამდენი იქნება ნაშთი გასაყოფის გაყოფის შემდეგ

print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)

#ლოგიკური ოპერატორი

requaired_pushups = 100
requaired_squats = 50

pushups = int(input)("how many pushups have u done")
squats = int(input)("how many squats have u done")

print(pushups == requaired_pushups and squats == requaired_squats)

#or version

target_pushups = 100
target_squats = 50 

print(pushups == target_pushups or squats == target_squats)

#or more version

print(pushups >= target_pushups or squats >= target_squats)