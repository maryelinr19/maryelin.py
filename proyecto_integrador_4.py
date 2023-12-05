import os

def convertir_mapa_a_matriz(mapa):
    return [list(fila) for fila in mapa.split("\n")]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_matriz(matriz):
    for fila in matriz:
        print("".join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial
    matriz_juego = [fila[:] for fila in mapa]  # Copia el mapa original para modificarlo

    while (px, py) != posicion_final:
        matriz_juego[px][py] = "P"  # Asignar el caracter "P" en la posición actual del jugador
        limpiar_pantalla()
        mostrar_matriz(matriz_juego)

        # Leer las teclas de flechas del teclado y actualizar la posición tentativa
        direccion = input("Ingresa una dirección (arriba: w, abajo: s, izquierda: a, derecha: d): ")
        nueva_px, nueva_py = px, py

        if direccion == "w":
            nueva_px -= 1
        elif direccion == "s":
            nueva_px += 1
        elif direccion == "a":
            nueva_py -= 1
        elif direccion == "d":
            nueva_py += 1

        # Verificar si la nueva posición tentativa es válida
        if (
            0 <= nueva_px < len(mapa) and
            0 <= nueva_py < len(mapa[0]) and
            mapa[nueva_px][nueva_py] != "#"
        ):
            matriz_juego[px][py] = "."  # Restaurar la posición anterior
            px, py = nueva_px, nueva_py
            matriz_juego[px][py] = "P"  # Actualizar la posición del jugador en el mapa

        # Limpiar la pantalla y mostrar el laberinto actualizado
        limpiar_pantalla()
        mostrar_matriz(matriz_juego)

    print("¡Felicidades, has llegado al final del laberinto!")

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_mapa_a_matriz(laberinto)
posicion_inicial = (1, 2)  # Actualiza la posición inicial según tu laberinto
posicion_final = (19, 18)  # Actualiza la posición final según tu laberinto

main_loop(mapa, posicion_inicial, posicion_final)
