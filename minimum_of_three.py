def min_of_three(*args):
    """This program returns the minimum of three numbers in an array"""
    for i in args:
        if i[0] < i[1] and i[0] > i[2]:
            print(i[0])
        elif i[1] < i[2]:
            print(i[1])
        else:
            print(i[2])


min_of_three([7, 3, 5], [15, 20, 40], [300, 550, 137])
