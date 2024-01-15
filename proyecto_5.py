import os
import random
import readchar

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final, nombre_jugador):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.nombre_jugador = nombre_jugador

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_matriz(self, matriz):
        for fila in matriz:
            print("".join(fila))

    def leer_tecla(self):
        while True:
            key = readchar.readkey()
            if key == readchar.key.UP:
                return "w"
            elif key == readchar.key.DOWN:
                return "s"
            elif key == readchar.key.LEFT:
                return "a"
            elif key == readchar.key.RIGHT:
                return "d"

    def main_loop(self):
        px, py = self.posicion_inicial
        matriz_juego = [fila[:] for fila in self.mapa]  # Copia el mapa original para modificarlo

        while (px, py) != self.posicion_final:
            matriz_juego[px][py] = "P"  # Asignar el caracter "P" en la posición actual del jugador
            self.limpiar_pantalla()
            self.mostrar_matriz(matriz_juego)

            # Leer las teclas de flechas del teclado y actualizar la posición tentativa
            direccion = self.leer_tecla()
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
                0 <= nueva_px < len(self.mapa) and
                0 <= nueva_py < len(self.mapa[0]) and
                self.mapa[nueva_px][nueva_py] != "#"
            ):
                # Limpiar la posición anterior del jugador y actualizar la posición actual
                matriz_juego[px][py] = "."
                px, py = nueva_px, nueva_py

        # Mostrar el mensaje de victoria al llegar a la posición final
        self.limpiar_pantalla()
        print(f"Felicidades, {self.nombre_jugador}! Has llegado a la meta.")

class JuegoArchivo(Juego):
    def __init__(self, ruta_mapas, nombre_jugador):
        self.ruta_mapas = ruta_mapas
        self.mapa = None
        self.posicion_inicial = None
        self.posicion_final = None
        self.leer_mapa_aleatorio()
        super().__init__(self.mapa, self.posicion_inicial, self.posicion_final, nombre_jugador)

    def leer_mapa_aleatorio(self):
        listas_mapas = os.listdir(self.ruta_mapas)
        nombre_mapa = random.choice(listas_mapas)
        ruta_mapa = os.path.join(self.ruta_mapas, nombre_mapa)

        with open(ruta_mapa, 'r', encoding='utf-8') as archivo:
            primeraLinea = next(archivo)
            posicion_x, posicion_y, final_x, final_y = (int(x) for x in primeraLinea.split())
            mapa = [list(linea.rstrip()) for linea in archivo]

            self.mapa = mapa
            self.posicion_inicial = (posicion_x, posicion_y)
            self.posicion_final = (final_x, final_y)

# Pedir el nombre del jugador por consola y mensaje de bienvenida
nombre_jugador = input("¡Bienvenido al juego de Laberintos! Por favor, ingresa tu nombre: ")
ruta_a_mapas = "mapas.txt"  # Reemplaza con la ruta correcta
juego_archivo = JuegoArchivo(ruta_a_mapas, nombre_jugador)
juego_archivo.main_loop()
