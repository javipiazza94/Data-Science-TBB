import math

def dias_semana(dias):
    if dias == 1:
        dia = 'Lunes'
    elif dias == 2:
        dia = 'Martes'
    elif dias == 3:
        dia = 'Miercoles'
    elif dias == 4:
        dia = 'Jueves'
    elif dias == 5:
        dia ='Viernes'
    elif dias == 6:
        dia = 'Sabado'
    elif dias == 7:
        dia = 'Domingo'
    else:
        dia = 'Introduce un numero del 1 al 7'
    return dia
        
dias_semana(4)

numero = int(input('introduce un numero para hacer la serie' ))

def numero_filas(numero):
    cont = 0
    for n in range(numero, 0, -1): 
        for i in range(n, 0, -1): 
            print(i, end=' ') 
        print()
        cont +=1
    return f'El numero de filas es: {cont}'    


def comparar_nummeros(num1, num2):
    if num1 == num2:
        resultado =  'Son iguales'
    if num1 > num2:
        resultado =  'El primer numero es mayor que el segundo'
    if num1 < num2:
        resultado = 'El segundo numero es mayor que el primero'
    return resultado

def contador_letra(texto, letra):
    cont = 0
    for l in texto:
        if l == letra:
            cont +=1
    return cont

def diccionario(palabra:str): 
    conver1 = list(palabra)
    cont = {}
    for i in conver1:
        cont[i] = conver1.count(i) #Para meterle un contador de letras a la palabra hay que asignar el valor del indice con el metodo count
    return cont

def modificar_lista(lista:list, comando:str, elemento=None): #Definimos por defecto tipos y valores
    """
    Añade o elimina elementos de una lista.

    Args:
        lista (list): La lista en la que se realizarán las modificaciones.
        comando (str): "add" para añadir un elemento o "remove" para eliminarlo.
        elemento: El elemento a añadir o eliminar. Por defecto es None.

    Returns:
        None
    """
    if comando == 'add' and elemento is not None:
        lista.append(elemento)
    elif comando == 'remove' and elemento is not None:
        try:
            lista.remove(elemento)
        except ValueError:
            print(f"El elemento '{elemento}' no se encuentra en la lista.")
    else:
        print("El comando debe ser 'add' o 'remove', y el elemento no debe ser None.")
        
def frase(*args):
   frase_completa = ''
   for i in args:
        frase_completa+=' '+i
   return frase_completa     

def fibonacci(numero):
    if numero < 2:
        resultado = numero
    else:
        resultado = fibonacci(numero-1) + fibonacci(numero-2)
    return resultado

#Area cuadrado
def area_cuadrado(lado):
    return math.pow(lado, 2)

#Area triangulo
def area_triangulo(base, altura):
    return (base*altura)/2

#Area circulo
def area_circulo(radio):
    return radio*math.pow(math.pi, 2)