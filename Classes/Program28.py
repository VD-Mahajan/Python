class Test:
    a=10
    @staticmethod
    def m1():
       #print(a)        Error : static method cannot access instance variables directly
        print(Test.a)
    
Test.m1()