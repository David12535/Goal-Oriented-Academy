def grow(arr):
    for number in arr[1:]:
        arr[0] *= number
    return arr[0]