import msvcrt  
import time


def input_tiempo(duracion=5):  
    print('presiona')  
    finaliza = time.time() + duracion 
    while time.time()< finaliza:
        if msvcrt.kbhit():
            print('Que desea hacer?: ')
            letra = int(msvcrt.getche())
            if letra == 1:
                print()
                print('Ganaste')
                break
            else:
                print('fallaste')

if __name__ == '__main__':
    input_tiempo()