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
       
    '''
    def __init__(self):
        '''
        Function that initializes attributes of class instances

        ...

        return: None
        '''
        self.sheep_count = 0

    def add_sheep(self):
        '''
        A function that counts sheep

        ...

       return: None
        '''
        self.sheep_count += 1
    
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
print(try_to_sleep.sheep_count)  
