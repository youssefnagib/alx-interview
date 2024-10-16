# 0x02. Minimum Operations

## Description

This repository contains a Python program that calculates the **minimum number of operations** needed to achieve exactly `n` characters in a file, starting with a single character 'H'. The operations allowed are:

- **Copy All**: You can copy all the characters you have.
- **Paste**: You can paste the characters you have copied.

The goal is to determine the fewest number of operations required to achieve exactly `n` characters.

## Learning Objectives

Through this project, you will:

- Understand the concept of **prime factorization**.
- Learn how to break down complex operations into simpler steps.
- Implement an algorithm to calculate the minimum operations.

## Requirements

- **Python 3.7+** is required to run the script.
- The program should run on all standard Linux-based environments.
- No external libraries are required.

## Files

### 1. `0-minoperations.py`
- **Objective**: Write a method `def minOperations(n)` that calculates the fewest number of operations needed to result in exactly `n` 'H' characters.
- **Description**: 
  - If `n` is impossible to achieve, return `0`.
  - Use the minimum operations based on a prime factorization approach.
  - Keep the time complexity as efficient as possible for large values of `n`.

### Example:

```python
n = 9
print(minOperations(n))  # Output: 6
