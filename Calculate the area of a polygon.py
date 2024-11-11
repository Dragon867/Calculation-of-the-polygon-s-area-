class Polygon:
    def __init__(self, vertices):
        """
        Initialize the Polygon object with a list of vertices.
        Each vertex is a tuple (x, y).
        """
        self.vertices = vertices
    
    def calculate_area(self):
        """
        Calculate and return the area of the polygon using the Shoelace Theorem.
        """
        n = len(self.vertices)  # Number of vertices
        area = 0
        
        # Apply Shoelace Theorem
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]  # Next vertex, looping back to 0 at the end
            area += x1 * y2 - y1 * x2
        
        area = abs(area) / 2.0  # The area must be positive, and we divide by 2
        return area

    def print_area(self):
        """
        Print the calculated area of the polygon.
        """
        area = self.calculate_area()
        print(f"The area of the polygon with vertices {self.vertices} is: {area:.2f}")


# Example usage:

# Vertices of a polygon (for example, a square or rectangle)
vertices = [(1, 1), (1, 4), (4, 4), (4, 1)]  # A rectangle with side lengths 3 and 3

# Create a Polygon object
polygon = Polygon(vertices)

# Print the area of the polygon
polygon.print_area()
