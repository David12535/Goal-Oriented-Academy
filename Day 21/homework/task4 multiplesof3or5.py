def solution(number):
    if number < 0:
        return 0
    summultiples = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            summultiples += num
    return summultiples