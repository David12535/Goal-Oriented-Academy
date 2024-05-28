#group14
#1
"""მომხმარებელს შემოატანინეთ ხუთი რიცხვი და შეიტანეთ ისინი სიაში. შემდეგ თქვენ უნდა იმუშაოთ ამ სიაზე:
 თუ რომელიმე ელემენტი სიაში ორჯერ მეორდება, დაამატეთ ის ახალ სიაში. საბოლოოდ გექნებათ ორი ვარიანტი: ცარიელი ახალი სია / ახალი სია სადაც 
 იქნება მინიმუმ ერთი ელემენტი.
 თუ სია ცარიელი იქნება, დაბეჭდეთ რომ სია ცარიელია. სხვა შემთხვევაში დაბეჭდეთ ახალი სია."""
def palindrome_checker(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

costumer_input = input("enter test case: ")
print(palindrome_checker(costumer_input))
#2
"""მომხმარებელს შემოატანინეთ ხუთი რიცხვი და შეიტანეთ ისინი სიაში. შემდეგ თქვენ უნდა იმუშაოთ ამ სიაზე: 
თუ რომელიმე ელემენტი სიაში ორჯერ მეორდება, დაამატეთ ის ახალ სიაში. საბოლოოდ გექნებათ ორი ვარიანტი: 
ცარიელი ახალი სია / ახალი სია სადაც იქნება მინიმუმ ერთი ელემენტი. თუ სია ცარიელი იქნება, 
დაბეჭდეთ რომ სია ცარიელია. სხვა შემთხვევაში დაბეჭდეთ ახალი სია."""

def manual_len(new_list):
    count = 0
    for i in new_list:
        count += 1
    return count


list = []
for i in range(5):
    num = int(input("Enter a number: "))
    list.append(num)

new_list = []
for element in list:
    if element in new_list:
        pass
    else:
        new_list.append(element)

if manual_len(new_list) == 0:
    print("Your list is empty")
else:
    print(new_list)

#3
"""მომხმარებელს შემოატანინეთ ხუთი სიტყვა. თქვენი დავალებაა, რომ ააწყოთ ახალი სიტყვა - 
თითოეულის პირველი ასო დაამატოთ მას. საბოლოოდ კი დაბეჭდოთ ეს სიტყვა.
test case: ["Hello", "this", "is", "best", "academy"] -> "Htiba"
test case: ["Join", "Goa", "and", "become", "chad"] -> "JGabc"""

new_string = ""

for i in range(5):
    string = input("Enter a word: ")
    new_string += string[0]

print(new_string)

#4
"""4.პირველ სიაში დაამატეთ 10-იდან 20-ის ჩათვლით არსებული ყველა მთელი რიცხვი. 
მეორე სიაში კი 30-იდან 50-ის ჩათვლით ყველა 5-ის ჯერადი. საბოლოოდ შეაერთეთ ეს ორი სია და დაბეჭდეთ ამ სახით."""

list1 = []
list2 = []
for i in range(10,20 + 1):
    list1.append(i)

for i in range(30,50 + 1):
    if i % 5 == 0:
        list2.append(i)

print(list1 + list2)

#group12
#1
"""შექმენით სია სადაც დაამატებთ სხვადასხვა ტიპის მონაცემებს, შემდეგ ეს დამატებული მონაცემები შეცვალეთ კიდევ სხვა მონაცემებით."""
data = []

data.extend(["ტექნოლოგია", 42, True, 3.14, {"სახელი": "ნიკა", "გვარი": "ხუციშვილი"}, [1, 2, 3, 4, 5]])

data = ["სამოქალაქო ტრანსპორტი", 73, False, 2.718, {"სახელი": "დავით", "გვარი": "ბერკაცაშვილი"}, [5, 4, 3, 2, 1]]

print(data)

#group 14
#1
"""explain:ვიწყებთ სიტყვით, ვთქვათ „ანა“.
ჩვენ ვქმნით ცარიელ ადგილს, სახელწოდებით reversed_word, რათა შევინახოთ სიტყვა საპირისპიროდ.
ჩვენ გავდივართ სიტყვაში თითოეულ ასოს, ბოლოდან დაწყებული.
ჩვენ ვამატებთ თითოეულ ასოს reversed_word-ს, ფაქტობრივად ვაბრუნებთ სიტყვას.
მას შემდეგ, რაც სიტყვას შევაბრუნებთ, ვადარებთ მას თავდაპირველ სიტყვას.
თუ შებრუნებული სიტყვა იგივეა, რაც თავდაპირველი სიტყვა, მაშინ სიტყვა არის პალინდრომი. წინააღმდეგ შემთხვევაში, ეს არ არის.
ასე რომ, ჩვენს მაგალითში "ანა", როდესაც მას ვაბრუნებთ, კვლავ ვიღებთ "ანას". ვინაიდან შებრუნებული სიტყვა იგივეა, 
რაც თავდაპირველი სიტყვა, დავასკვნით, რომ „ანა“ არის პალინდრომი."""
word = "ანა"
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[index]

if word == reversed_word:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")

#2
"""მიიღეთ ნომრები: სთხოვეთ მომხმარებელს 5 ნომერი, შეინახეთ ისინი სიაში სახელწოდებით numbers_list.
იპოვეთ განმეორებითი ნომრები: გადახედეთ თითოეულ რიცხვს ნომრების_სიაში.
შეამოწმეთ რამდენჯერ გამოჩნდება თითოეული რიცხვი სიაში.
თუ რიცხვი არაერთხელ გამოჩნდება და ის უკვე არ არის repeat_value სიაში, დაამატეთ იგი repeat_value-ს.
განმეორებითი ნომრების ამობეჭდვა: ამობეჭდეთ რიცხვები, რომლებიც გაიმეორეს.
ასე რომ, პროგრამა ძირითადად აგროვებს ციფრებს, ამოწმებს რომელი ჩნდება ერთზე მეტჯერ და ბეჭდავს ამ განმეორებით რიცხვებს."""
numbers_list = []
repeat_value = []

for i in range(5):
    num = int(input("Please enter number: "))
    numbers_list.append(num)


for number in numbers_list:
    count = numbers_list.count(number)
    if count > 1 and number not in repeat_value:
        repeat_value.append(number)

print(repeat_value)

seats = 10
while seats > 0:
    seats = seats - 1
    print ("seat equpt")

#1
"""შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ.
 აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში."""
def even_sum(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 == 1:
            sum += i
    return sum

print(even_sum([1,2,3,4,5,6,7,8,9,10]))

#2
"""შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის."""
def even_or_odd(num):
    if num % 2 == 0:
        return "Your number is even"
    else:
        return "Your number is odd"
#3
"""შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს)."""
def prime_detecor(num):
    if num % 2 == 0 and num % 3 == 0:
        return "Your number isn't prime"
    else:
        return "Your number is prime"
print(prime_detecor(10))
print(prime_detecor(7))

#4
"""შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. თქვენი დავალებაა, 
რომ დააბრუნოთ ამ სიის განახლებული ვერსია, სადაც ყველა სახელი დიდი ასოთი დაიწყება."""

def name_fixer(names):
    updated_list = []
    for name in names:
        updated_list.append(name.capitalize())
    return updated_list

print(name_fixer(["david", "chad", "gigachad"]))
#5
"""შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ 
ამ სიის ყველა რიცხვი - თუ რიცხვი ლუწია, ახალ სიაში დაამატეთ მისი განაყოფი ორზე, 
ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. საბოლოოდ დააბრუნეთ განახლებული სია"""
def func(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num/2)
        else:
            new_list.append(num*2)
    return new_list

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))