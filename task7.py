class TrafficLight:
    '''
    Class of TrafficLight

    ...

    Attributes:
    permissible_values : list
                list of colors
       
    '''
    permissible_values = ['Зеленый', 'Желтый', 'Красный']

    def __init__(self):
        '''
        Function that initializes attributes of class instances

        '''
        self.current_signal = 'Зеленый'
        self.previous_signal = 'Желтый'

    def next_signal(self):
        '''
        Function that get new color 

        ...

        return : self.current_signal
        '''
        if self.current_signal == 'Зеленый':
            self.previous_signal = 'Зеленый'
            self.current_signal = 'Желтый'
        elif self.current_signal == 'Желтый':
            if self.previous_signal == 'Зеленый':
                self.previous_signal = 'Желтый'
                self.current_signal = 'Красный'
            else:
                self.previous_signal = 'Желтый'
                self.current_signal = 'Зеленый'
        elif self.current_signal == 'Красный':
            self.previous_signal = 'Красный'
            self.current_signal = 'Желтый'

    def __str__(self):
        '''
        String representation method
        '''
        return f'TrafficLight(current_signal = {self.current_signal})'
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()


traffic_light = TrafficLight()
print(traffic_light)

for color in range(10):
    traffic_light.next_signal()
    print(traffic_light)