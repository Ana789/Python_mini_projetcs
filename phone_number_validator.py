import re  # Import the 're' module for regular expression operations

# Your code starts here
ui = input()  # Take user input and store it in the variable 'ui'

# Define a regular expression pattern 'h'
# ^         - Asserts the start of the string
# 07        - Matches the exact characters '07'
# \d{8}     - Matches exactly eight digits (0-9)
# $         - Asserts the end of the string
h = r"^07\d{8}$"

# Use 're.match()' to check if the input 'ui' matches the pattern 'h'
if re.match(h, ui):
    print("Valid")  # Print "Valid" if the input matches the pattern
else:
    print("Invalid")  # Print "Invalid" if the input does not match the pattern
