class Dog:
    '''
    Class of dogs

    ...

    Attributes:
    name : str
            name of the dog

    Methods:
    say(self):
       Prints 'Гав!'
    '''
    def __init__(self, name=None):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        name : str
               name of the dog

        '''
        self.name = name

    def say(self):
        '''
       The printing function Гав!

       ...

       return: None
        '''
        return f'{self.name}: Гав!'
    
    def __str__(self):
        '''
        String representation method
        '''
        return f'Dog(name = {self.name})'
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()

dog = Dog('Барбос')
print(dog.say())