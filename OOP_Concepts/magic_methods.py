class Rectangle:
    def __init__(self, length, width):
        """Initializing the length and width of the rectangle."""
        self.length = length
        self.width = width

    @property
    def area(self):
        """Calculating the area of the rectangle."""
        return self.length * self.width

    @property
    def perimeter(self):
        """Calculating the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    def __eq__(self, other):
        """Comparing two rectangles based on their area."""
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False


# Creating two rectangle instances with different dimensions
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(2, 7)

# Demonstrating the use of property methods
print("Rectangle 1:")
print(rectangle1)  # This should now work without errors
print("Area:", rectangle1.area)
print("Perimeter:", rectangle1.perimeter)

print("\nRectangle 2:")
print(rectangle2)
print("Area:", rectangle2.area)
print("Perimeter:", rectangle2.perimeter)

# Comparing the two rectangles
if rectangle1 == rectangle2:
    print("\nBoth rectangles have the same area.")
else:
    print("\nThe rectangles have different areas.")
