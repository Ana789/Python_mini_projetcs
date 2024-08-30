# Define a class named 'Juice' to represent a type of juice with a name and capacity
class Juice:
    # Constructor method to initialize the Juice object with a name and capacity
    def __init__(self, name, capacity):
        self.name = name  # Sets the name of the juice
        self.capacity = capacity  # Sets the capacity of the juice in liters

    # Method to provide a string representation of the Juice object
    def __str__(self):
        # Returns the juice's name and capacity in the format "JuiceName (CapacityL)"
        return self.name + ' (' + str(self.capacity) + 'L)'

    # Overloaded '+' operator method to combine two Juice objects
    def __add__(self, newJuice):
        # Combines the names of both juices with an '&' symbol
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
