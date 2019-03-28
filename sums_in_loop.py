def sum_pairs(arr1, arr2):
    """This program returns the sum of two numbers from different lists located at the same index"""
    pairs = []
    for i in range(len(arr1)):
        pairs.append(arr1[i] + arr2[i])
    return pairs


print(sum_pairs([1, 2, 3], [4, 5, 6]))
