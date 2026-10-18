Password Requirements Checker

A small command-line Python program that checks whether a password meets rules chosen by the user. You set a minimum length and decide whether the password must contain numbers and special characters.

> Despite the project name, this script checks a password you enter; it does not generate one.

## Features

- Set the minimum password length.
- Choose whether numbers are required.
- Choose whether special characters are required.
- Get a clear result showing whether the password meets the selected requirements.

## Requirements

- Python 3

The script uses Python's built-in `string` module, so no extra packages are needed.

## Run the program

Save the code as `password_checker.py`, then run:

```bash
python password_checker.py
```

Depending on your setup, you may need to use `python3` instead of `python`.

## Example

```text
Enter the minimum length: 10
Should your password contain numbers? (y/n): y
Should your password contain special characters? (y/n): y
Create your password: Example123!
Your password meets the requirements.
```

## How it works

The `check_password` function checks the password's length and, when selected, looks for at least one digit and at least one punctuation character. The program prints whether all selected requirements are met.
