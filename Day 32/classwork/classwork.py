def validate_pin(pin):
    for i in pin:
        if i < '0' or i > '9':
            return False
        else:
            return True
def manual_isdigit(element):
    num_list = [1,2,3,4,5,6,7,8,9]
    if element in num_list:
        return True
    else:
        return False