#!/usr/bin/python3
'''
This module contains a function to
calculate the minimum number of operations
required to reach exactly n 'H' characters
in a file, starting with a single 'H'.
'''
def minOperations(n: int) -> int:
    '''
    Calculate the minimum number of operations
    required to reach exactly n 'H' characters
    in a file, starting with a single 'H'.
    argument:
    n (int): The target number of 'H' characters
    return:
    int: The minimum number of operations to reach n 'H' characters
    '''
    if n <= 1:
        return 0
    divied =2
    operation = 0
    
    while n > 1:
        while n % divied == 0:
            operation += divied
            n = n // divied
        divied += 1

    return operation
