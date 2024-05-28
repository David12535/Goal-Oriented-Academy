def square_digits(num):
    squareddigits_str = ""
    numstr = str(num)
    for digit in numstr:
        squareddigits_str += str(int(digit)**2)
    return int(squareddigits_str)