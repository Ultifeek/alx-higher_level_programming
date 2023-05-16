#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    find = []

    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            find.append(True)
        else:
            find.append(False)

    return (find)
