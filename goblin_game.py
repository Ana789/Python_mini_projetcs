"""
This module defines a `Juice` class that represents different types of juice, allowing for the creation of juice objects with specific names and capacities.

The class provides functionality for:
- Displaying juice objects in a user-friendly format.
- Combining two juice objects into a single one using the overloaded '+' operator.

Example usage:
- Create juice objects and combine them to get a new juice object with the combined name and capacity.
"""
class Juice:
    """
    A class to represent a type of juice with a name and capacity.

    Attributes:
        name (str): The name of the juice (e.g., 'Orange').
        capacity (float): The capacity of the juice in liters (e.g., 1.5L).

    Methods:
        __str__(): Returns a string representation of the juice object, showing its name and capacity.
        __add__(other): Overloads the '+' operator to combine two Juice objects into one.
    """

    def __init__(self, name, capacity):
        """
        Initializes a new Juice object with the given name and capacity.

        Args:
            name (str): The name of the juice.
            capacity (float): The capacity of the juice in liters.
        """
        self.name = name  # Sets the name of the juice
        self.capacity = capacity  # Sets the capacity of the juice in liters


    def __str__(self):
        """
        Returns a string representation of the Juice object.

        The string is formatted as "JuiceName (CapacityL)", where JuiceName is the name of the juice
        and Capacity is its capacity in liters.

        Returns:
            str: The formatted string representing the Juice object.
        """
        return self.name + ' (' + str(self.capacity) + 'L)'

    # Overloaded '+' operator method to combine two Juice objects
    def __add__(self, newJuice):
        """
        Overloads the '+' operator to combine two Juice objects.

        This method combines the names and capacities of two Juice objects and returns a new Juice object
        with the combined name and capacity.

        Args:
            newJuice (Juice): Another Juice object to combine with.

        Returns:
            Juice: A new Juice object with the combined name and capacity.
        """
        combined_name = self.name + "&" + str(newJuice.name)
        # Adds the capacities of both juices
        combined_capacity = self.capacity + newJuice.capacity
        # Creates and returns a new Juice object representing the combination
        return Juice(combined_name, combined_capacity)


# Create two Juice objects, 'a' and 'b'
a = Juice('Orange', 1.5)  # Juice object 'a' with name 'Orange' and capacity 1.5L
b = Juice('Apple', 2.0)  # Juice object 'b' with name 'Apple' and capacity 2.0L

# Combine the two Juice objects using the overloaded '+' operator
# and print the result using the __str__ method of the new Juice object
print(a + b)  # Output: "Orange&Apple (3.5L)"
