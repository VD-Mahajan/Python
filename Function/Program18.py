class Demo:
    def __str__(self):
        return 'str'

    def __repr__(self):
        return f'Instance of {self.__class__}'


print(Demo())           #=====> Instance of <class '__main__.Demo'>


'''

class Demo:
    def __repr__(self):
        return f'Instance of {self.__class__}'
        
    def __str__(self):
        return 'str'

print(Demo())       ===> Instance of <class '__main__.Demo'>
'''