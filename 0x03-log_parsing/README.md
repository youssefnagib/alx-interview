# 0x03. Log Parsing

## Description
This project involves building a Python script to parse HTTP log files. The script reads from standard input (stdin) line by line and computes statistics such as the total file size and counts of specific HTTP status codes. It prints out these metrics every 10 lines or upon a keyboard interruption (`CTRL + C`).

## Requirements
- Python 3.x
- The script must handle the following input format:
- After every 10 lines and/or a keyboard interruption, it prints:
- The total file size processed.
- The count of HTTP status codes in ascending order:
  - 200
  - 301
  - 400
  - 401
  - 403
  - 404
  - 405
  - 500

## Example

Running the script with a log generator:
