# 0x0A. Prime Game

## Description

This project involves implementing a game that revolves around prime numbers. Players take turns choosing prime numbers from a list, and each choice affects the subsequent moves. The goal is to determine the winner based on the game's rules and logic.

## Learning Objectives

* Understand prime numbers and their properties.
* Implement efficient algorithms for primality testing.
* Work with game theory concepts in programming.
* Optimize performance for large input sizes.

## Requirements

* Python 3.8+
* Code should comply with PEP 8 standards.

## Files

### `prime_game.py`

This file contains the implementation of the Prime Game.

### `tests/test_prime_game.py`

This directory contains test cases to validate the functionality of the game.

## Game Rules

1. The game starts with a list of numbers from `1` to `n`.
2. Players take turns choosing a prime number from the list.
3. Upon choosing a prime number, all its multiples are removed from the list.
4. The game ends when no moves are possible.
5. The player unable to make a move loses the game.

## Function Signature

```python
def isWinner(x, nums):
    """
    Determines the winner of the game.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of integers representing the range of numbers for each round.

    Returns:
        str: Name of the winner ("Maria" or "Ben") or None if there's no winner.
    """
```

### Parameters

* `x`: The number of rounds to play.
* `nums`: A list where each element represents the maximum number in the range for that round.

### Return Value

* Returns the name of the winner ("Maria" or "Ben") based on the number of wins.

## Example

```python
>>> from prime_game import isWinner
>>> isWinner(3, [4, 5, 1])
"Maria"
```

In this example:

* Round 1: Range is 1 to 4.
* Round 2: Range is 1 to 5.
* Round 3: Range is 1 to 1.

Maria wins the game.

## Algorithm Explanation

1. **Prime Number Generation**:
   * Use the Sieve of Eratosthenes to generate all primes up to the maximum number in `nums` efficiently.
2. **Game Simulation**:
   * Simulate each round by tracking the remaining numbers and determining valid moves.
3. **Score Calculation**:
   * Count the number of wins for each player.

## Testing

Run the test cases using `unittest`:

```bash
python3 -m unittest discover tests
```

## Authors

* **Youssef Nagib**

## License

This project is licensed under the MIT License - see the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.
