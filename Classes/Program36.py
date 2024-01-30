class Test:
    a = 10

    @staticmethod
    def m1():
        print(a)   #NameError: name 'a' is not defined.  To remove error => Test.a

Test.m1()