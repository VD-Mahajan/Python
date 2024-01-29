class Test:
    a=10
    @staticmethod
    def m1():
        print(a)  # Error : static method cannot access instance variables directly
    
Test.m1()