#!/usr/bin/python3
'''
Validate a list of integers representing UTF-8 encoded data.

The function should return True if all the integers in the list form
a valid UTF-8 encoded string,
False otherwise.'''


def validUTF8(data):
    '''
    Validate a list of integers representing UTF-8 encoded data.'''
    def count_leading_ones(num):
        '''counts the number'''
        count = 0
        for i in range(7, -1, -1):
            if (num >> i) & 1:
                count += 1
            else:
                break
        return count

    i = 0
    while i < len(data):
        leading_ones = count_leading_ones(data[i])

        if leading_ones == 0:
            i += 1
            continue
        elif leading_ones == 1 or leading_ones > 4:
            return False

        for j in range(1, leading_ones):
            if i + j >= len(data):
                return False
            if (data[i + j] & 0b11000000) != 0b10000000:
                return False
        i += leading_ones

    return True
