#!/usr/bin/python3
'''
def canUnlockAll(boxes):
'''


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    This function takes a list of boxes,
    where each box is represented by a list of keys.
    Parameters:
    boxes (List[List[int]]): A list of boxes,
    where each box is represented by a list of keys.
    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    # Initialize a set to track unlocked boxes
    unlocked = set()
    # Start with the first box which is unlocked
    unlocked.add(0)

    # Initialize a list to keep track of boxes to check
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        # Get the current key
        key = keys.pop()
        # If the key opens a box that is not already unlocked
        if key < len(boxes) and key not in unlocked:
            # Unlock that box
            unlocked.add(key)
            # Add its keys to the list of keys to check
            keys.extend(boxes[key])

    # Return True if all boxes can be unlocked
    return len(unlocked) == len(boxes)
