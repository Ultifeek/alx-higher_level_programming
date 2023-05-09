#!/usr/bin/python3
def remove_char_at(str, n):
    j = ""
    for c in range(len(str)):
        if c != n:
            j = j + str[c]
    return (j)
