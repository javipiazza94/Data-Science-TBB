class Tienda:
    # Variables de clase
    """
    Metemos las dos variables solidad de la clase Tienda: Tipo y Abierta

    Returns:
        Tipo(Str): Es el tipo de tienda que es
        Abierta(bool): Devuelve si está abierta o cerrada
    """
    Tipo = "Electrodomésticos"
    Abierta = True
    
    def __init__(self, nombre:str, direccion:str, num_empleados:int, ventas_tres_meses:list):
        """
        Constructor de la clase Tienda.

        Args:
            nombre (str): El nombre de la tienda.
            direccion (str): La dirección de la tienda.
            num_empleados (int): El número de empleados.
            ventas_tres_meses (list): Una lista de ventas de los últimos tres meses.
        """
        # Variables de instancia
        self.nombre = nombre
        self.direccion = direccion
        self.num_empleados = num_empleados
        # Parsea los valores de ventas a números decimales y almacena los últimos tres meses
        self.ventas = [float(v) for v in ventas_tres_meses[:3]]
        
    #Metodos de clase
    def suma_ventas(self):
        """
        Calcula las ventas anuales sumando las ventas de los últimos tres meses.

        Returns:
            float: El total de ventas anuales.
        """
        ventas_anuales = 0
        for n in self.ventas:
            ventas_anuales += n
        # Alternativamente, puedes usar la función integrada sum: return sum(self.ventas)
        return ventas_anuales
    
    def avg_ventas_empleado(self):
        """
        Calcula el promedio de ventas por empleado.

        Returns:
            float: El promedio de ventas por empleado.
        """
        return sum(self.ventas) / self.num_empleados
    
    def obtener_datos(self):
        """
        Obtiene el nombre y la dirección de la tienda como una cadena formateada.

        Returns:
            str: Una cadena formateada que contiene el nombre y la dirección de la tienda.
        """
        return f"{self.nombre}, {self.direccion}"
    
    def obtener_ventas_ultimo_mes(self):
        """
        Obtiene las ventas del último mes.

        Returns:
            float: Las ventas del último mes.
        """
        return self.ventas[2]
    
    def proyeccion_ventas(self, x):
        """
        Proyecta las ventas futuras basándose en un multiplicador 'x'.

        Args:
            x (float): El multiplicador para la proyección.

        Returns:
            float: Las ventas proyectadas.
        """
        if x < 1000:
            proyeccion = self.suma_ventas() * 1.2  # Si deseas calcular los meses individualmente, usa una comprensión de lista como: [1.2 * v for v in self.ventas]
        else:
            proyeccion = self.suma_ventas() * 1.5
        return proyeccion


class Perro:
    """
    Esta clase representa a un perro con características comunes.

    Attributes:
        num_patas (int): El número de patas que tiene el perro (predeterminado es 4).
        num_orejas (int): El número de orejas que tiene el perro (predeterminado es 2).
        num_ojos (int): El número de ojos que tiene el perro (predeterminado es 2).
        velocidad (float): La velocidad actual del perro (predeterminada es 0).

    """
    # Variables de clase comunes a todos los perros
    num_patas = 4
    num_orejas = 2
    num_ojos = 2
    velocidad = 0

    def __init__(self, nombre, raza, pelo="Marrón", dueño=False):
        """
        Constructor de la clase Perro.

        Args:
            nombre (str): El nombre del perro.
            raza (str): La raza del perro.
            pelo (str, opcional): El color del pelo del perro (predeterminado es "Marrón").
            dueño (bool, opcional): Si el perro tiene un dueño o no (predeterminado es False).
        """
        self.nombre = nombre
        self.raza = raza
        self.pelo = pelo
        self.dueño = dueño

    def andar(self, aumento_velocidad):
        """
        Aumenta la velocidad actual del perro.

        Args:
            aumento_velocidad (float o int): La cantidad en la que se aumentará la velocidad.

        Returns:
            float: La nueva velocidad del perro después de aumentarla en aumento_velocidad.
        """
        return self.velocidad + aumento_velocidad

    def parar(self):
        """
        Detiene al perro y establece su velocidad en cero.

        Returns:
            float: La velocidad del perro después de detenerlo, que será igual a cero.
        """
        return self.velocidad

    def ladrar(self, entrada):
        """
        Hace que el perro ladre.

        Args:
            entrada (str): La cadena que se incluirá en el ladrido del perro.

        Returns:
            str: Una cadena que representa el ladrido del perro con la entrada proporcionada.
        """
        return f"GUAU {entrada}"