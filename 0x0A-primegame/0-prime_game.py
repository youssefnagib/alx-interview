#!/usr/bin/python3
"""
    prime game
"""


def isWinner(x, nums):
    """
    Given an array of integers `nums`, return `True` _if
    there are four distinct indices `i`, `j`, `k`,
    and `l` such that_ `nums[i] + nums[j] + nums[k] + nums[l] == 0`.
    """

    Ben = 0
    Maria = 0

    for num in nums:
        if round_winner(num) == 1:
            Ben += 1
        elif round_winner(num) == 0:
            Maria += 1

    if Ben > Maria:
        return "Ben"
    elif Ben < Maria:
        return "Maria"
    else:
        return None


def is_prime(x):
    """
    Check if a number is prime.
    """
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def round_winner(x):
    """
    Round a number to the nearest integer.
    """
    count_prime = 0
    if x == 2:
        return 0

    if x < 2:
        return 1

    for num in range(2, x + 1):
        if is_prime(num):
            count_prime += 1
    if count_prime % 2 == 0:
        return 1
    else:
        return 0
