def letrero(a):
    b = 50
    print('=' * b)
    print(a.center(b, '='))
    print('=' * b)

def menu(a):
    b = 50 - int(len(a))
    print(a.center(b, ' '))