class User:
    '''
    Class of User

    ...

    Attributes:
    id : str
               name of the dog
        nick_name : str
                users nick name 
        first_name : str
                users first name
        last_name=None : str
                users last name 
        middle_name=None : str
                users middle name 
        gender=None : str
                users gender 

    '''

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        id : str
               name of the dog
        nick_name : str
                users nick name 
        first_name : str
                users first name
        last_name=None : str
                users last name 
        middle_name=None : str
                users middle name 
        gender=None : str
                users gender 
        '''
        self.id = id 
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name 
        self.middle_name = middle_name
        self.gender = gender

    def update(self, **kwargs):
        '''
        Function that updates values

        ...

        Parameters:
        kwargs : dictionary
                parameters that are passed by name
        
        return : None

        '''
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        '''
        String representation method
        '''
        return f"User(id={self.id}, nick_name='{self.nick_name}',\
first_name='{self.first_name}', last_name='{self.last_name}',\
middle_name='{self.middle_name}', gender='{self.gender}')"
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()
    
user = User(1, "user123", "Alice", last_name="Smith", gender="female")
print(user)

user.update(nick_name="new_nick", last_name="Johnson")
print(user)      
    
