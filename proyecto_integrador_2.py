import readchar

while True:
    tecla = readchar.readkey()
    print(tecla)
    if tecla == '\x1b[A':  # Código de la tecla ↑ (UP)
        break

    # En este código, utilizamos la función readkey() de la biblioteca readchar para leer un carácter del teclado. El carácter leído se almacena en la variable tecla. Luego, imprimimos la tecla utilizando print(). Si la tecla presionada es la tecla ↑ (UP), que se representa con el código \x1b[A, salimos del bucle utilizando break