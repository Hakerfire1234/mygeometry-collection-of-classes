import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def move_point(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

    def midpoint(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Coordinate(mx, my)

class Line:
    def __init__(self, coordinate1: Coordinate, coordinate2: Coordinate):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def plot_line(self, color: str):
        plt.plot([self.coordinate1.x, self.coordinate2.x], [self.coordinate1.y, self.coordinate2.y], color=color)

    def line_length(self):
        return ((self.coordinate1.x - self.coordinate2.x)**2 + (self.coordinate1.y - self.coordinate2.y)**2)**0.5

class Shape:
    class Quadrilateral:
        def __init__(self, point1: Coordinate, point2: Coordinate, point3: Coordinate, point4: Coordinate):
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
            self.point4 = point4

        def plot_quadrilateral(self, fill=False, color='black'):
            x_values = [self.point1.x, self.point2.x, self.point3.x, self.point4.x, self.point1.x]
            y_values = [self.point1.y, self.point2.y, self.point3.y, self.point4.y, self.point1.y]

            if fill:
                plt.fill(x_values, y_values, color=color)
            else:
                plt.plot(x_values, y_values, color=color)

        def area(self):
            x_values = [self.point1.x, self.point2.x, self.point3.x, self.point4.x, self.point1.x]
            y_values = [self.point1.y, self.point2.y, self.point3.y, self.point4.y, self.point1.y]
    
            return 0.5 * abs(sum(x_values[i] * y_values[i + 1] - x_values[i + 1] * y_values[i] for i in range(4)))
        
    class Polygon:
        def __init__(self, *vertices):
            self.vertices = vertices

        def plot_polygon(self, fill=False, color='black'):
            x_values = [vertex.x for vertex in self.vertices]
            y_values = [vertex.y for vertex in self.vertices]

            if fill:
                plt.fill(x_values, y_values, color=color)
            else:
                plt.plot(x_values, y_values, color=color)

class Plane:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = []

    def add_point(self, coordinate: Coordinate):
        if coordinate.x <= self.x and coordinate.y <= self.y:
            self.coordinates.append(coordinate)
        else:
            raise IndexError("Coordinate is not on the plane scale")
        
    def plot_points(self):
        for coordinate in self.coordinates:
            plt.plot(coordinate.x, coordinate.y, 'ro')
        plt.xlim(0, self.x)
        plt.ylim(0, self.y)
        plt.grid()

    def label(self, x: str, y: str):
        plt.xlabel(x)
        plt.ylabel(y)

    def show_plot(self):
        plt.show()
