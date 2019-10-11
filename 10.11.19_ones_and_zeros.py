""" Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1. """

def binary_array_to_number(arr):
    c = 0
    for i in range(0,len(arr)):
        n = 2**((len(arr)-1)-i)*arr[i]
        c += n
    return c
