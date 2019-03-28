def find_min(*args):
    """This program finds the minimum of two numbers in a given array"""
    for i in args:
        if i[0] < i[1]:
            print(i[0])
        else:
            print(i[1])


find_min([3, 5], [7, 1], [4, 2])
