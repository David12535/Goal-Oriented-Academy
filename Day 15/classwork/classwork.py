# დავალება1) შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით
# (ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.

for i in range(0, 20 + 1):
               print(i)


# დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ
#  ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
for i in range(1, 20 + 1):
    if i % 2 == 0:
     print(i)


# დავალება3) შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი 
# (დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი
# # უარყოფითი index-ების საშუალებით.

my_arrary = []

for number in range(50, 101):
    my_arrary.append(number)

    print(my_arrary[-5:])


# დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვის 
# start-ის, ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ. ახლა ჩაურთეთ if statement და 
# დაპრინტეთ მარტო ხუთის ჯერადები.



num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
start = (min(num1, num2))
end = (max(num1, num2))

for i in range(start, end + 1):
    if i % 5 == 0:
      print(i)   




# დავალება5) შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება,
# შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.



name_array = []
age = int(input("enter your age: "))

if age > 18:
   name = input("enter your name: ")
   name_array.append(name)
   print("name in the array:", my_arrary)
else:
    print("you are not eligible to provide a name" )





# დავალება2: მომხმარებელს შეეკითხეთ რიცხვი. შემდეგ for ციკლით 
# start პოზიციად ეს რიცხვი, ხოლო end-ად ამ რიცხვზე ათით მეტი აიღეთ და 
# ყველა რიცხვი ჩაამატეთ ახალ სიაში. სიიდან გამოიტანეთ ელემენტები 2 ინდექსის
# გამოტოვებითაი ესენია


user_num = int(input("first number: "))
second_num = user_num + 10

new_list = []
for i in range(user_num, second_num + 1):
     new_list.append(i)
print(new_list[::2])     