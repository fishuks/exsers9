class Game:
    '''
    Class of Game

    ...

    Attributes:
    teams :  dictionary
            name of the commands
    score :  dictionary
            score of the game
    '''

    def __init__(self, teams):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        teams :  dictionary
            name of the commands
        
        '''
        self.teams = teams
        self.score = {'command1':0, 'command2':0}

    def ball_thrown(self, points, command):
        '''
        Function that adds points

        ...

        Parameters:
        points : int
                point of the game
        command : str
                command that gets points
        
        return : None

        '''
        self.score[command] += points

    def get_score(self):
        '''
        Function that return score

        ...

        rerurn : self.score.values()
        '''

        return (tuple(self.score.values()))
    
    def det_winner(self):
        '''
        Function that chose winner

        ...

        return : name of command or Ничья!
        '''
        if self.score['command1'] > self.score['command2']:
            return f'Победила {self.teams["command1"]}'
        elif self.score['command1'] < self.score["command2"]:
            return f'Победила {self.teams}'
        else:
            return 'Ничья!!'
        
    def __str__(self):
        '''
        String representation method

        '''
        return f'Teams = {self.teams}, score = {self.score}'
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()
        
teams = {
    'command1': 'мама',
    'command2': 'папа'
}
game = Game(teams)      
game.ball_thrown(3, 'command1')
print(game.get_score())
print(game.det_winner())
help(Game)
