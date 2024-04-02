class MorseMsg:
    '''
    Class of MorseMsg
    ...

    Attributes:
   encoded_message : str 
            massege
       
    '''
    def __init__(self, encoded_message):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
         encoded_message : str 
            massege
        '''
        self.encoded_message = encoded_message
        self.translate_ru = []
        self.translate_eng = []

    def eng_decode(self):
        '''
         Function that decode from english

        ...

        Parameters:
         encoded_message : str 
            massege

        return : translate_eng

        '''
        english = { 'A' : '.-',
                    'B' : '-...',
                    'C' : '-.-.',
                    'D' : '-..',
                    'E' : '.',
                    'F' : '..-.',
                    'G' : '--.',
                    'H' : '....',
                    'I' : '..',
                    'J' : '.---',
                    'K' : '-.-',
                    'L' : '.-..',
                    'M' : '--',
                    'N' : '-.',
                    'O' : '---',
                    'P' : '.--.',
                    'Q' : '--.-',
                    'R' : '.-.',
                    'S' : '...',
                    'T' : '-',
                    'U' : '..-',
                    'V' : '...-',
                    'W' : '.--',
                    'X' : '-..',
                    'Y' : '-.--',
                    'Z' : '--..'
        }
        message_split = self.encoded_message.split()
        for letter in message_split:
            for key, value in english.items():
                if letter == value:
                    self.translate_eng.append(key)
        return self.translate_eng
    
    def ru_decode(self):
        '''
         Function that decode from russian

        ...

        Parameters:
         encoded_message : str 
            massege

        return : translate_ru
        '''
        russian = { 'А' : '.-',
                    'Б' : '-...',
                    'Ц' : '-.-.',
                    'Д' : '-..',
                    'Е' : '.',
                    'Ф' : '..-.',
                    'Г' : '--.',
                    'Х' : '....',
                    'И' : '..',
                    'Й' : '.---',
                    'К' : '-.-',
                    'Л' : '.-..',
                    'М' : '--',
                    'Н' : '-.',
                    'О' : '---',
                    'П' : '.--.',
                    'Щ' : '--.-',
                    'Р' : '.-.',
                    'С' : '...',
                    'Т' : '-',
                    'У' : '..-',
                    'Ж' : '...-',
                    'В' : '.--',
                    'Д' : '-..',
                    'Ы' : '-.--',
                    'З' : '--..',
                    'Ч' : '---.',
                    'Ш' : '----',
                    'Ъ' : '.--.-.',
                    'Ь' : '-..-',
                    'Э' : '..-..',
                    'Ю' : '..--',
                    'Я' : '.-.-'
        }
       
        message_split = self.encoded_message.split()
        for letter in message_split:
            for key, value in russian.items():
                if letter == value:
                    self.translate_ru.append(key)
        return self.translate_ru
    
    def get_volwels(self, lang):
        '''
         Function that return volwels

        ...

        Parameters:
         lang : str 
                language

        return :  volwels 
        '''
        volwels = []
        if lang == 'ru':
            for letter in 'aоуыэеёиюя'.upper ():
                if letter in self.translate_ru:
                    volwels.append(letter)
            return volwels
        
        elif lang == 'eng':
            for letter in 'aoeiuy'.upper ():
                if letter in self.translate_eng:
                    volwels.append(letter)
            return volwels
        
    def get_consonats(self, lang):
        '''
         Function that return consonats

        ...

        Parameters:
         lang : str 
                language

        return : consonats
        '''
        consonats = []
        if lang == 'ru':
            for letter in 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
                if letter in self.translate_ru:
                    consonats.append(letter)
            return consonats
        
        elif lang == 'eng':
            for letter in 'bcdfghjklmnpqrstvwxyz'.upper ():
                if letter in self.translate_eng:
                   consonats.append(letter)
            return consonats
    def __str__(self):
        '''
        String representation method
        '''
        f'{self.translate_ru}, {self.translate_eng}'

    def __repr__(self):
        '''
        String representation method
    
        '''
        return self.__str__()
                    


mass = MorseMsg('-- -.--  -. .- -- .  .. ...  ... --- -. -.-- .-')

print(mass.ru_decode())
print(mass.get_volwels(lang='ru'))
print(mass.get_consonats(lang= 'ru'))

print(mass.eng_decode())
print(mass.get_volwels(lang= 'eng'))
print(mass.get_consonats(lang= 'eng'))