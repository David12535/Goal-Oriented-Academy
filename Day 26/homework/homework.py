"""1. Manual Sum Function: Create a function called manual_sum that iterates over list and adds their sum in a variable, 
then returns variable. Use for loop for this task."""

def manual_sum(list):             
    sum = 0
    for i in list:
        sum += i
    return sum

print(manual_sum([21,22,23,24,25,26,27,28,29,30]))

"""2. Manual Max Function: Define a function named manual_max that iterates through list, 
updating a variable with the maximum value, then returns the maximum value found. Use for loop for this task."""

def manual_max(list):
    high_number = list[0] 
    for i in list:
        if high_number < i:
            high_number = i
    return high_number

"""3. Manual Min Function: Define a function named manual_min that iterates through list, 
updating a variable with the minimum value, then returns the minimum value found. Use for loop for this task."""


def manual_min(number):
    small_number = number[0] 
    for i in list:
        if small_number > i:
            small_number = i
    return small_number

print(manual_min([7,2,15,15,16,7,1,2,2,18]))


"""4. Manual Len Function: Develop a function named manual_len that iterates through list, counting each element, 
and returns the count as the length of the list. Use for loop for this task."""


def manual_len(list):
    count = 0
    for i in list:
        count += 1
    return count

print(manual_len([12,10,125,265,18,9]))

"""5. Copy function of reduce: define a function named manual_reduce that takes a list as input, 
then create an empty list named copied_list to store the copied items inside it. 
Then use for loop to loop over each item in the original list, append them to the copied_iterable list. 
In the end, return the copied_iterable after iterating through all items.
finally demonstrate the usage of the manual_reduce function by creating an original list, 
making a copy of it, and printing both the original and copied lists."""

def normal_reduce(numbers):
    copied = []
    for i in list:
        copied.append(i)
    numbers += "]"
    numbers += "["
    for i in copied:
        numbers.append(i)
    return numbers 
    