import numpy as np
import string
import random
from tabulate import tabulate
from variables import AGUA_ICON, BARCO_ICON, TAM_BARCOS, SHOOT_ICON, FAIL_ICON

class Tablero:
    def __init__(self, size=11):
        self.size = size
        self.matriz = np.full((self.size, self.size), " ", dtype=str)
        self.inicializar_tablero()

    def inicializar_tablero(self):
        letras = list(string.ascii_uppercase)[:self.size-1]
        self.matriz[0, 1:] = letras
        numeros = np.arange(1, self.size)
        self.matriz[1:, 0] = numeros.astype(str)

    def colocar_barcos_aleatoriamente(self):
        for longitud, cantidad in TAM_BARCOS:
            for _ in range(cantidad):
                self._colocar_barco_aleatorio(longitud)
        # Opcional: Rellenar agua explícitamente si se desea, 
        # pero ' ' ya se trata como agua desconocida.
        # self.matriz[self.matriz == " "] = AGUA_ICON 

    def _colocar_barco_aleatorio(self, longitud):
        while True:
            fila, columna, orientacion = self._generar_posicion(longitud)
            if self._es_colocacion_valida(fila, columna, longitud, orientacion):
                self._colocar_barco(fila, columna, longitud, orientacion)
                break

    def _colocar_barco(self, fila, columna, longitud, orientacion):
        for i in range(longitud):
            r, c = fila, columna
            if orientacion == "N":
                r -= i
            elif orientacion == "S":
                r += i
            elif orientacion == "E":
                c += i
            elif orientacion == "O":
                c -= i
            self.matriz[r, c] = BARCO_ICON.get(longitud, "O")

    def _generar_posicion(self, longitud):
        fila = random.randint(1, self.size - 1)
        columna = random.randint(1, self.size - 1)
        orientacion = random.choice(["N", "S", "E", "O"])
        return fila, columna, orientacion

    def _es_colocacion_valida(self, fila, columna, longitud, orientacion):
        # Verificar limites y superposicion
        for i in range(longitud):
            r, c = fila, columna
            if orientacion == "N":
                r -= i
            elif orientacion == "S":
                r += i
            elif orientacion == "E":
                c += i
            elif orientacion == "O":
                c -= i
            
            if not (1 <= r < self.size and 1 <= c < self.size):
                return False
            if self.matriz[r, c] != " ":
                return False
        return True

    def imprimir_tablero(self):
        print(tabulate(self.matriz, headers="firstrow", tablefmt='fancy_grid'))


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vidas = sum(longitud * cantidad for longitud, cantidad in TAM_BARCOS)
        self.fallos = 0
        self.aciertos = 0
        self.tablero_barcos = Tablero()
        self.tablero_disparos = Tablero()  # Donde marco mis disparos
        
        self.tablero_barcos.colocar_barcos_aleatoriamente()

    def recibir_disparo(self, fila, columna):
        """
        Procesa un disparo recibido en las coordenadas dadas.
        Retorna el estado del disparo: 'agua', 'tocado', 'hundido' (simplificado a tocado para este juego), o 'repetido'.
        """
        celda = self.tablero_barcos.matriz[fila, columna]
        
        if celda in [SHOOT_ICON, FAIL_ICON, AGUA_ICON]:
            return "repetido"
        
        if celda != " " and celda != AGUA_ICON:
            # Tocado
            self.tablero_barcos.matriz[fila, columna] = SHOOT_ICON
            self.vidas -= 1
            return "tocado"
        else:
            # Agua
            self.tablero_barcos.matriz[fila, columna] = FAIL_ICON # Marcamos el fallo en el tablero de barcos tambien? A veces ayuda.
            return "agua"

    def registrar_disparo(self, fila, columna, resultado):
        """
        Actualiza el tablero de disparos del jugador segun el resultado.
        """
        if resultado == "tocado":
            self.tablero_disparos.matriz[fila, columna] = SHOOT_ICON
            self.aciertos += 1
        elif resultado == "agua":
            self.tablero_disparos.matriz[fila, columna] = FAIL_ICON
            self.fallos += 1
        # Si es repetido no hacemos nada o mostramos mensaje fuera

    def mostrar_stats(self):
        print(f"JUGADOR: {self.nombre} | Vidas Restantes: {self.vidas} | Aciertos: {self.aciertos}")

class Maquina(Jugador):
    def __init__(self):
        super().__init__("Lord Vader")
    
    def generar_disparo_aleatorio(self, tablero_objetivo):
        """Genera coordenadas validas de disparo que no hayan sido usadas antes."""
        # Simple random strategy for now
        while True:
            fila = random.randint(1, 10)
            columna = random.randint(1, 10)
            # Verificamos en nuestro tablero de disparos si ya tiramos ahi
            if self.tablero_disparos.matriz[fila, columna] == " ":
                return fila, columna
