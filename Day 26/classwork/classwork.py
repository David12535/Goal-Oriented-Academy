"""დავალება: შექმენით პროგრამა, სადაც ბოლოდან პირველ ოთხის ჯერად რიცხვს გამოიტანთ სიიდან.
 მაგ სიაში კი 10-იდან 50-ის ჩათვლით უნდა იყოს რიცხვები"""
def numbers():
    numbers_list= []
    list = []
    for i in range(10,50+1):
        list.append(i)
    for i in range(len(list) -1,-1,-1):
        if i % 4 == 0:
            numbers_list.append(i)
    return numbers_list[0]
print(numbers())

numbers = []

for i in range(10, 50+1):
    numbers.append(i)
print(numbers)

"""დავალება: შექმენით range-ის მსგავსი ფუნქცია, სადაც მესამე არგუმენტი იქნება მომხმარებლის მიერ შეტანილი. 
აგრეთვე კომენტარით აღწერეთ return"""
def range(start,end,step=1):
    list = []
    while start < end:
        list.append(start)
        start += step
    return list

print(range(1,10,2))
#


"""დავალება2: შექმენით ფუნქცია სახელად filter, მისი პირველი პარამეტრი იქნება კოლექცია, მეორე კი მნიშვნელობა.
 თქვენი დავალებაა, რომ კოლექციიდან ამოიღოთ ეგ კონკტეტული მნიშვნელობები და დააბრუნოთ ის"""

def filter(start,end):
    new_list = []
    for i in start:
        if i == end:
            pass
        else:
            new_list.append(i)
    return new_list
print(filter([7,4,4,4,5,1,1,1,2],2))

"""დავალება3: შექმენით ფუნქცია, 
რომელსაც გადასცემთ მართკუთხა სამკუთხედის კათეტებს, თქვენი დავალება კი არის ის, რომ დააბრუნოთ ჰიპოტენუზა. a^2 + b^2 = c^2"""

def calcurator_multiply(num1,num2):
    num1_squared = num1 ** 2
    num2_squared = num2 ** 2
    hypotenuse = num1_squared + num2_squared
    hypotenuse_squared = hypotenuse ** 0.5
    return hypotenuse_squared
print(calcurator_multiply(6,8))














"""დავალება4: შექმენით ფუნქცია, რომელსაც გადაეცემა თქვენი სახელი. თუ სახელის სიგრძე აღემატება ხუთს, დააბრუნეთ მისი uppercase ვარიანტი.
 ხოლო თუ ნაკლებია ან ტოლია მისი, დააბრუნეთ capitalize ვარიანტი"""
def name_filter(name):
    if len(name) > 7:
        return name.upper()
    else:
        return name.capitalize()

print(name_filter("David"))

















