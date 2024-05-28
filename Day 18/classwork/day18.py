def num_list_creator():
    amount = int(input("Enter how many numbers you want to enter in list: "))

    list = []

    for i in range(amount):
        i = int(input("Enter number you want to add to list: "))
        list.append(i)
    return list

------------------------------------------------------
def num_list_creator():
    amount = int(input("Enter how many numbers you want to enter in list: "))

    list = []

    for i in range(amount):
        i = int(input("Enter number you want to add to list: "))
        if i > 10 and i % 2 == 0:
            list.append(i)
    return list
--------------------------------------------------------
def sort_list(numbers):

    for i in range(len(numbers)):
        if numbers[i] > numbers[i + 1]:
            temp = numbers[i + 1]
            numbers[i + 1] = numbers[i]
            numbers[i] = temp

    return numbers
--------------------------------------------------------
def squared_numbers(numbers):
    squared_numbers_list = []

    for num in numbers:
        squared_numbers_list.append(num * num)
    
    return squared_numbers_list

print(squared_numbers([1,2,3,4,5]))
def strings_length(strings_list):
    length_list = []

    for word in strings_list:
        length_list.append(len(word))
    
    return length_list

print(strings_length(["luka","nia","giorgi","lile"]))
def sum_of_numbers(numbers):
    result = 0

    for num in numbers:
        if num > 10:
            result = result + num
    
    return result

print(sum_of_numbers([1,2,3,11,15,5]))


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
