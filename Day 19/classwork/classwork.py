def even_indexes(lastname):
    even_index_chars = []

    for index in range(len(lastname)):
        if index % 2 == 0:
            even_index_chars.append(lastname[index])
    
    return even_index_chars


lastname = input("Please enter lastname: ")

print(even_indexes(lastname))
def even_indexes(lastname):
    even_index_chars = []

    for index in range(len(lastname)):
        if index % 2 == 0:
            even_index_chars.append(lastname[index])
    
    return '+'.join(even_index_chars)


lastname = input("Please enter lastname: ")

print(even_indexes(lastname))
def even_indexes(lastname):
    result = ''

    for index in range(len(lastname)):
        if index % 2 == 0:
            result = result + lastname[index]
    
    return result


lastname = input("Please enter lastname: ")

print(even_indexes(lastname))





