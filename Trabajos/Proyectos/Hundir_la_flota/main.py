from clases import Jugador, Maquina
from funciones import jugar 

def main():
    print("----- Bienvenido a Hundir la flota -----")
    print("Tienes que derribar 8 barcos, ¡que comience la batalla!")

    normas_del_juego = """
    Normas del Juego:
    1. El objetivo es hundir los barcos del oponente antes de que él hunda los tuyos.
    2. Cada jugador tiene una flota de barcos distribuidos en el tablero.
    3. En cada turno, un jugador elige una coordenada para disparar.
    4. Si aciertas en una coordenada ocupada por un barco enemigo, impactas el barco.
    5. Si hundes completamente un barco enemigo, ganas un punto (en esta versión simplificada, se restan vidas).
    6. El juego termina cuando un jugador ha hundido todos los barcos del oponente.
    7. ¡Que gane el mejor!
    """

    print(normas_del_juego)
    
    nombre_jugador = input("Dígame su nombre, Maestro Jedi: ")
    if not nombre_jugador:
        nombre_jugador = "Jugador 1"
        
    # Instanciación de jugadores (Los tableros se crean internamente)
    jugador = Jugador(nombre=nombre_jugador)
    maquina = Maquina()

    print("\nInformación del Jugador:")
    # Mostrar tablero con barcos propios
    jugador.tablero_barcos.imprimir_tablero()
    
    # print("\nInformación de la Máquina (Debug - Barcos):")
    # maquina.tablero_barcos.imprimir_tablero()

    # Iniciar juego
    jugar(jugador, maquina)


if __name__ == "__main__":
    main()


