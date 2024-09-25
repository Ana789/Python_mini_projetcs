"""
This module converts a temperature from Celsius to Fahrenheit.

- First, it reads an integer input from the user, which represents the temperature in Celsius.
- Then, it defines a function `conv` that converts
the Celsius temperature to Fahrenheit using the formula:
  Fahrenheit = (1.8 * Celsius) + 32
- The converted Fahrenheit value is printed inside the function.

The conversion is demonstrated in two ways:
1. By using the `conv` function.
2. By performing the calculation directly outside the function,
with the result printed to the console.

Usage:
- The user is prompted to input a temperature in Celsius.
- The conversion and results are displayed both
through the function call and the direct calculation.
"""

# Read an integer input from the user, which represents the temperature in Celsius.
celsius_input = int(input())


# Define a function `conv` that takes a Celsius temperature as an argument.
def conv(celsius_temp):
    """
    Convert a temperature from Celsius to Fahrenheit and print the result.

    Args:
        celsius (int or float): The temperature in Celsius to be converted.

    Conversion Formula:
        Fahrenheit = (1.8 * Celsius) + 32

    Prints:
        The corresponding temperature in Fahrenheit.
    """

    fahrenheit_temp = (1.8 * celsius_temp) + 32

    # Print the calculated Fahrenheit value.
    print(fahrenheit_temp)


# Call the `conv` function with the user-provided Celsius value to convert and print it.
conv(celsius_input)

# Alternatively, directly calculate the Fahrenheit value without using the function.
fahrenheit_result = (1.8 * celsius_input) + 32

# Print the Fahrenheit value calculated outside the function.
print(fahrenheit_result)
