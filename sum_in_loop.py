def sum_nums(arr):
    """This program returns the sum of an array of numbers"""
    total = 0
    for i in arr:
        total += i
    return total


print(sum_nums([3, 4, 5, 6]))
