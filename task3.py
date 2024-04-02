class NotSleeping:
    '''
    Class of NotSleeping

    ...

    Attributes:
    sheep_count : int
           count of sheeps

    Methods:
    add_sheep(self):
            method that counts sheep
    lost(self):
            method that resets the counter
    get_count_sheeps(self):
            method that outputs the number of sheep

    '''
    def __init__(self):
        '''
        Function that initializes attributes of class instances

        '''
        self.sheep_count = 0

    def add_sheep(self):
        '''
         Function that counts sheep
        '''
        self.sheep_count += 1

    def lost(self):
        '''
        Function that resets the counter

        ...

        return: None
        '''
        self.sheep_count = 0

    def get_count_sheeps(self):
        '''
        Function that outputs the number of sheep

        ...

        return: self.sheep_count
        '''
        return self.sheep_count
    
    def __str__(self):
        '''
        String representation method

        '''
        return f'Count of sheeps = {self.sheep_count}'
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()

try_to_sleep = NotSleeping()
for sheep in range(10):
    try_to_sleep.add_sheep()  
print(try_to_sleep.get_count_sheeps())
try_to_sleep.lost()
print(try_to_sleep.get_count_sheeps())  
