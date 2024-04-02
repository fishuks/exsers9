class Point:
    def __init__(self, tuple_coordinates = (0,0)):
        self.tuple_coordinates = tuple_coordinates
        self.x = tuple_coordinates[0]
        self.y = tuple_coordinates[1]
        

    def get_x(self):
        return int(self.x)
    
    def get_y(self):
        return int(self.y)
    
    def distance(self, other):
        x_self = int(self.x)
        y_self = int(self.y)
        x_other = int(other[0])
        y_other = int(other[1])
        return ((x_other - x_self)**2 + (y_other - y_self)**2)**(1/2)
    
    def sum(self, other):
        new_x = int(self.tuple_coordinates[0]) + int(other[0])
        new_y = int(self.tuple_coordinates[1]) + int(other[1])
        return (new_x, new_y)

    def __str__(self):
         return f'Point(Coordinates = ({self.x},{self.y}))' 
    
class Segment(Point):
    def __init__(self, point: Point, other):
        super().__init__(point.tuple_coordinates)
        super().sum(other)
        
    def __str__(self):
        return f'Segment(Coordinates1 = {self.tuple_coordinates}, Coordinates2 = {point.sum()})'
    
point = Point(tuple_coordinates=(2, 3))
print(point)
print(point.distance(other=(2, 6)))
seg = Segment(point, (2, 6))
print(seg)



