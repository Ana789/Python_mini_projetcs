# Read an integer input from the user, which represents the temperature in Celsius.
celsius = int(input())


# Define a function `conv` that takes a Celsius temperature as an argument.
def conv(celsius):
    # Calculate the Fahrenheit equivalent using the conversion formula.
    # Fahrenheit = (1.8 * Celsius) + 32
    fahrenheit = (1.8 * celsius) + 32

    # Print the calculated Fahrenheit value.
    print(fahrenheit)


# Call the `conv` function with the user-provided Celsius value to convert and print it.
conv(celsius)

# Alternatively, directly calculate the Fahrenheit value without using the function.
fahrenheit = (1.8 * celsius) + 32

# Print the Fahrenheit value calculated outside the function.
print(fahrenheit)
