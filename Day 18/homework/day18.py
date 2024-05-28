"""შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. თქვენ უნდა დააბრუნოთ გაფილტრული სია,
 სადაც უკვე მარტო 4-ის ჯერადები იქნება."""

def four_filter(list):
    new_list = []
    for i in range(len(list)):
        if i % 4 == 0:
            new_list.append([i])
    return new_list

print(four_filter([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

#შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.

def user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name : ")
    data_list = []
    data_list.append(first_name)
    data_list.append(last_name)
    return data_list

"""მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას, 
for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ გაფილტვრა, 
ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში 
დაამატეთ მისი მეორე ხარისხი, ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი)."""

start_num = int(input("Enter a starting number: "))
end_num = int(input("Enter ending number: "))

even_list = []
odd_list = []

for i in range(start_num,end_num):
    if i % 2 == 0:
        a = i * i
        even_list.append(a)
    else:
        b = i ** 0.5
        odd_list.append(b)

print("Squares of even numbers are",even_list)
print("Roots of odd numbers are",odd_list)

"""შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო 
გადაიტანეთ ახალ სიაში. შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე - მარტო ლუწ 
ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.
Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ."""

def last_name_transformer(last_name):
    new_list = []
    for i in range(len(last_name)):
        if i % 2 == 0:
            new_list.append(last_name[i])
        string_convert = str(new_list)
    return string_convert

print(last_name_transformer("berkacashvili"))

#შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ჯამი / სიგრძე

def average_calculator(num_list):
    average = sum(num_list) / len(num_list)
    return average


"""შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, მაგ: word - drow.
 საბოლოდ კი დააბრუნეთ შედეგი."""

def string_reverser():
    string = input("Enter a word: ").lower()
    reversed_string = string[::-1]
    print(reversed_string)
    return reversed_string

string_reverser()


"""შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას, რომელსაც არ ექნება დუპლიკატები
 (ერთი და იგივე ელემენტები). """

def duplicate_remover(list):
    new_list = []
    for i in range(len(list)):
        if list[i] in new_list:
            pass
        else:
            new_list.append(list[i])
    return new_list


print(duplicate_remover([1,2,3,4,4,4,4,5]))