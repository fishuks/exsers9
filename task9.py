class StrandsDNA:
    '''
    Class of StrandsDNA

    ...

    Attributes:
   all_strands : list
            list of strands
    '''
    def __init__(self):
        '''
        Function that initializes attributes of class instances

        '''
        self.all_strands = []

    def add_strands(self, strands):
        '''
         Function that add strands

        ...

        Parameters:
        strands : str 
            strands of dna

        return : None

        '''
        strands_split = strands.split()
        for strand in strands_split:
            if strand not in self.all_strands:
                self.all_strands.append(strand)

    def get_max_strands(self):
        '''
         Function that get list of strands with max len

        ...

        return : None

        '''
        lengths = []
        max_strands = []
        for strand in self.all_strands:
            lengths.append(len(strand))
        max_length = max(lengths) 
        for strand in self.all_strands:
            if len(strand) == max_length:
                max_strands.append(strand)
        sorted(max_strands)
        return ' '.join(max_strands)   
    
    def __str__(self):
        '''
        String representation method

        '''
        return f'List of strads = {self.all_strands}'
    
    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()

dna = StrandsDNA()
dna.add_strands("AGT CGT AGT CGT AGT") 
dna.add_strands("AGT CGT AGT AGT") 
print(dna.get_max_strands())     


    