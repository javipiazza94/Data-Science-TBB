# Pedimos la palabra secreta y calculamos su longitud
PalabraSecreta = input("Introduce la palabra secreta: ")
NLetrasPalabraSecreta = len(PalabraSecreta)

# Creamos una lista de guiones bajos para representar las letras ocultas. Multiplicamos los espacios por el numero de palabras par crear la sustitucion
PalabraGuiones = ['_'] * NLetrasPalabraSecreta
print(' '.join(PalabraGuiones))  # Imprimimos los guiones separados por espacios

# Inicializamos las variables para el juego
JuegoTerminado = False
intentos = 3
index = NLetrasPalabraSecreta #Variable auxiliar para poder trabajar con ella

# Comenzamos el bucle principal
while not JuegoTerminado:
    if index != 0:
        print("Te quedan", intentos, "intentos")
        print(' '.join(PalabraGuiones))
        
        #Introducimos la letra y la comparamos a traves de un for.
        letra = input("Introduce una letra: ")
        
        #Este booleano nos permitira realizar comparaciones si acertamos o no
        XLetraAcertada = False

        for j in range(NLetrasPalabraSecreta):
            if PalabraSecreta[j] == letra: #Si coincide la letra dada por la original
                PalabraGuiones[j] = letra #Sustituimos el guion por la letra
                index -= 1
                XLetraAcertada = True

        if not XLetraAcertada:
            print("No has acertado ninguna letra")
            intentos -= 1
            if intentos > 0:
                if intentos < 3:
                    print("     *   ")
                    print("   *   * ")
                    print("  *     *")
                if intentos < 2:
                    print("  *******")
                    print("  *     *")
                    print("  *     *")
                    print("  *     *")
            else:
                print("PERDISTE")
                JuegoTerminado = True
                print("     *   ")
                print("   *   * ")
                print("  *     *")
                print("  *******")
                print("  *     *")
                print("  *     *")
                print("  *     *")
                print("  *     *")
                print("*         *")
                print("*         *")
    else:
        print("Has ganado, la palabra secreta es", PalabraSecreta)
        JuegoTerminado = True


                
                
				

