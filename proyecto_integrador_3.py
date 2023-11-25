import os
import readchar

def borrar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')

numero = 0

while numero <= 50:
    borrar_terminal()
    print(numero)
    tecla = readchar.readkey()
    if tecla == 'n':
        numero += 1
