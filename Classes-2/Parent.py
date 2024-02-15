import moduleDemo


class Parent:

    def __init__(self):
        print('In Parent')


if __name__ == '__main__':
    moduleDemo.Demo()
else:
    Parent()
