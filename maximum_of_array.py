def max_and_min(arr):
    """This program returns the maximum and minimum numbers in an array"""
    max_num = arr[0]
    min_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num


print(max_and_min([3, 4, 5, 1, 18, 23, 43, 12, 5, 32, 54, 8, 435, 2, 9]))
