'''
we can use any name in place of self
'''


class Student:
    def __init__(delf):
        delf.name = 'Vishal'
        delf.roll_no = 37
        delf.marks = 89
    def talk(self):
        print(f'Hello my name is {self.name}')
        print(f'My roll no is {self.roll_no}')
        print(f'and my marks are {self.marks}')
        
obj = Student()
obj.talk()