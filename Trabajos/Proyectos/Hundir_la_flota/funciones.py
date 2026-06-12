from variables import NUMERO_FILAS, NUMERO_COLUMNAS
import time
import numpy as np

def turno_manual(jugador, enemigo):
    """
    Gestiona el turno del jugador humano.
    """
    print(f"\n--- Turno de {jugador.nombre} ---")
    
    # Mostrar tablero de disparos del jugador (donde ha disparado antes)
    print("Tu mapa de disparos:")
    jugador.tablero_disparos.imprimir_tablero()
    
    letras = 'ABCDEFGHIJ'
    diccionario_letras_numeros = dict(zip(letras, np.arange(1, 11)))
    
    while True:
        try:
            coord_col = input("Introduce columna (A-J): ").upper()
            if coord_col not in diccionario_letras_numeros:
                console_print("Columna inválida. Debe ser de A a J.")
                continue
                
            coord_fila_input = input(f"Introduce fila (1-10): ")
            if not coord_fila_input.isdigit():
                 console_print("Fila inválida. Debe ser un número.")
                 continue
            
            coord_fila = int(coord_fila_input)
            
            if not (1 <= coord_fila <= 10):
                console_print("Fila fuera de rango.")
                continue
                
            columna = diccionario_letras_numeros[coord_col]
            fila = coord_fila
            
            # Procesar disparo
            resultado = enemigo.recibir_disparo(fila, columna)
            
            if resultado == "repetido":
                console_print("¡Ya has disparado a esta coordenada! Intenta otra.")
                continue
            
            # Registrar en mi tablero
            jugador.registrar_disparo(fila, columna, resultado)
            
            if resultado == "tocado":
                console_print("¡TOCADO! Has dado en el blanco.")
                # winsound.Beep(1000, 200) # Optional: Sound
                return True # Repite turno si toca? En reglas estandar si, en este codigo original parecia que no explicito pero "Siguiente turno" si fallaba.
                            # El original decia: si no disparo (fallo) -> siguiente turno. Si disparo (acierto) -> break loop pero no next turn?
                            # Espera, linea 121 original: `disparo = disparar...` if not disparo: sig turno. else: loop continues?
                            # No, en original `while not fin_del_juego` wraps turns.
                            # Si aciertas, te mantienes en tu turno?
                            # En el original: if not disparo: siguiente turno. else: ... no saltaba 'continue', seguia a turno jugador 2.
                            # Ah, veo el codigo original:
                            # Turno J1 -> if miss: print fail. else: print hit.
                            # Turno J2 -> ...
                            # No habia "vuelve a tirar si aciertas".
                            # Vamos a mantener reglas simples: 1 tiro por turno.
                return True
            elif resultado == "agua":
                console_print("¡AGUA! Disparo al mar.")
                return False
                
        except Exception as e:
            print(f"Error inesperado: {e}")
            break

def turno_maquina(maquina, jugador):
    """
    Gestiona el turno de la IA.
    """
    print(f"\n--- Turno de {maquina.nombre} ---")
    time.sleep(1)
    
    fila, columna = maquina.generar_disparo_aleatorio(jugador.tablero_barcos)
    
    # Convertir a coordenadas legibles para el usuario
    letras = ' ABCDEFGHIJ' # Ojo espacio en 0
    letra_col = letras[columna]
    print(f"{maquina.nombre} dispara a {letra_col}{fila}...")
    time.sleep(1)
    
    resultado = jugador.recibir_disparo(fila, columna)
    maquina.registrar_disparo(fila, columna, resultado)
    
    if resultado == "tocado":
        console_print("¡TE HAN DADO! Tu barco ha sido impactado.")
        return True
    elif resultado == "agua":
        console_print("¡LA MÁQUINA HA FALLADO! Se ha ido al agua.")
        return False
    else:
        # Repetido, no deberia pasar con la logica actual de la IA
        return False

def console_print(msg):
    """Helper para prints con sleep un poco mas cinematico"""
    print(msg)
    time.sleep(1.5)

def jugar(jugador, maquina):
    print("¡COMIENZA LA BATALLA NAVAL!")
    
    turno_jugador = True # Empieza jugador
    
    while jugador.vidas > 0 and maquina.vidas > 0:
        if turno_jugador:
            acierto = turno_manual(jugador, maquina)
            # Si queremos que repita turno al acertar:
            # if not acierto: turno_jugador = False
            # Por ahora cambio de turno siempre para simplificar y match original flow
            turno_jugador = False
        else:
            acierto = turno_maquina(maquina, jugador)
            turno_jugador = True
            
        # Mostrar estado
        print("\nEstado actual:")
        jugador.mostrar_stats()
        maquina.mostrar_stats()
        
        # Check win condition inmediato
        if maquina.vidas == 0:
            print(f"\n¡FELICIDADES {jugador.nombre}! HAS HUNDIDO LA FLOTA ENEMIGA. ¡VICTORIA!")
            break
        if jugador.vidas == 0:
            print(f"\n¡{maquina.nombre} HA GANADO! TU FLOTA HA SIDO DESTRUIDA.")
            break
            
        # Pausa entre turnos
        print("-" * 30)
        time.sleep(1)

