def product_of_nums(list):
    product_of_nums = 1 
    for num in list:
        product_of_nums *= num
    return product_of_nums

print(product_of_nums([2, 5, 3, 5, 3, 10, 2]))


#1 
def sum_of_nums(list):
    sum_of_nums = 1
    for num in list:
        sum_of_nums += num
    return sum_of_nums
print(sum_of_nums([18, 14, 15, 14, 16]))

#2
def filter(strings_list):
    filtered_list=[]
    for word in strings_list:
        if len(word) > 5:
            filtered_list.append(word)
    return filtered_list
print(filter(["David", "hokage", "raikage", "nugzara"]))       

#3
def Odd_numbers(numbers):
    Odd_numbers_list = [2, 4 , 6]

    for num in numbers:
        if num % 2 == 0:
            Odd_numbers_list.append(num)

            return Odd_numbers_list
print(Odd_numbers([12,15,18,17,22,25]))

#4
def largest_number(numbers):
    max_number = numbers[0]
    for num in numbers:
        if max_number < num:
            max_number=num
            return max(numbers)

print(largest_number([12,24,17,4,5,27,7,8,9,40]))

#5
def filter_list(strings_list):
    filtered_list = []

    for word in strings_list:
        if word[0] == 'a':
            filtered_list.append(word)

    return filtered_list

words = ["anakonda", "majlajuna", "pitoni", "ajganda", "anuki=anakonda"]
print(filter_list(words))

#6
def squared_numbers(numbers):
    squared_numbers_list = []

    for num in numbers:
        squared_numbers_list.append(num * num)

    return squared_numbers_list

print(squared_numbers([1,2,3,4,5]))

#7
def strings_length(strings_list):
    length_list = []
 
    for word in strings_list:
        length_list.append(len(word))

    return length_list
print(strings_length(["maria,", "saba", "luka", "oqroa", "namcxvari"]))

#8
def sum_of_numbers(numbers):
    result = 0

    for num in numbers:
        if num > 10:
            result = result + num
    
    return result

print(sum_of_numbers([1,2,3,11,15,5]))