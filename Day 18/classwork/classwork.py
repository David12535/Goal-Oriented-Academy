# დავალება: შექმენით პროგრამა, სადაც მომხმარებელს შემოატანინებთ თუ რამდენ რიცხვს შეიტანენ სიაში. შემდეგ შექმენით სია, for ციკლში input-ით
#  შეეკითხეთ რიცხვი და შეიტანეთ ამ სიაში ეს რიცხვები. ბოლოს სიის ჯამი დააბრუნეთ 

def filter_evens(numbers):
    filtered_list = []

    for num in numbers:
        if num >= 10 and num % 2 == 0:
            filtered_list.append(num)
    
    return filtered_list

def sum_of_numbers(numbers):
    sum = 0

    for i in numbers:
        sum = sum + i
    
    return sum

count = int(input("Please enter how many numbers do you want to input: "))

numbers = []

for i in range(count):
    number = int(input("Please enter number: "))
    numbers.append(number)


print(sum_of_numbers(numbers))
print(filter_evens(numbers))