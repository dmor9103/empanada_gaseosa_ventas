from os import system

def letrero(a, b):
    system('cls')
    print('=' * b)
    print(a.center(b, '='))
    print('=' * b)
    print('')

def menu(a):
    b = 50 - int(len(a))
    print(a.center(b, ' '))