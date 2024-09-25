"""
This module checks if a user-inputted phone number follows a specific format using regular expressions.

The format being validated is a phone number that:
- Starts with '07'.
- Is followed by exactly 8 digits (0-9).
- Has no other characters before or after the number.

The `re` module is used to match the input against the defined regular expression pattern.

Key functionality:
- Takes user input.
- Validates the input against the pattern using the `re.match()` function.
- Prints 'Valid' if the input matches the phone number format, otherwise prints 'Invalid'.

Pattern breakdown:
- ^: Asserts the start of the string.
- 07: Matches the exact string '07'.
- \d{8}: Matches exactly eight digits (0-9).
- $: Asserts the end of the string.
"""

import re  # Import the 're' module for regular expression operations

# Your code starts here
ui = input()  # Take user input and store it in the variable 'ui'

# Define a regular expression pattern 'h'
# ^         - Asserts the start of the string
# 07        - Matches the exact characters '07'
# \d{8}     - Matches exactly eight digits (0-9)
# $         - Asserts the end of the string
H = r"^07\d{8}$"

# Use 're.match()' to check if the input 'ui' matches the pattern 'h'
if re.match(H, ui):
    print("Valid")  # Print "Valid" if the input matches the pattern
else:
    print("Invalid")  # Print "Invalid" if the input does not match the pattern
