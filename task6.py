class Point:
    '''
    Class of Point

    ...

    Attributes:
    tuple_coordinates :  tuple
            coordinates of point 
    '''

    def __init__(self, tuple_coordinates = (0,0)):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
         tuple_coordinates :  tuple
                coordinates of point 
        '''
        self.tuple_coordinates = tuple_coordinates
        self.x = tuple_coordinates[0]
        self.y = tuple_coordinates[1]
        

    def get_x(self):
        '''
         Function get X coordinates

        ...
        
        return : self.x
        '''
        return int(self.x)
    
    def get_y(self):
        '''
         Function get Y coordinates

        ...
        
        return : self.y
        '''
        return int(self.y)
    
    def distance(self, other):
        '''
        Function get distance

        ...

        Parameters:
            other:  tuple
                coordinates of other point 
        
        return : distance
        
        '''
        x_self = int(self.x)
        y_self = int(self.y)
        x_other = int(other[0])
        y_other = int(other[1])
        distance = ((x_other - x_self)**2 + (y_other - y_self)**2)**(1/2)
        return distance
    
    def sum(self, other):
        ''''
         Function get sum

        ...

        Parameters:
            other:  tuple
                coordinates of other point 
        
        return : (new_x, new_y)
        '''
        new_x = int(self.tuple_coordinates[0]) + int(other[0])
        new_y = int(self.tuple_coordinates[1]) + int(other[1])
        return (new_x, new_y)

    def __str__(self):
        '''
        String representation method
        '''
        return f'Point(Coordinates = ({self.x},{self.y}))' 
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()
    
    
point = Point(tuple_coordinates=(2, 3))
print(point)
print(point.distance(other=(2, 6)))
print(point.sum(other=(2,6)))



