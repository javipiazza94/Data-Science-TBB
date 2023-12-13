# Definir los valores
valor_presente = 1.0
valor_futuro = 0.60
num_anios = 22

# Calcular la tasa de inflación anualizada
tasa_inflacion_anualizada = ((valor_futuro / valor_presente) ** (1 / num_anios) - 1) * 100

# Imprimir el resultado
print(f"La tasa de inflación anualizada es aproximadamente {tasa_inflacion_anualizada:.2f}%")


#########################################################################################################

# Definir los valores
aportacion_mensual = 250.0
tasa_interes_anual = 0.0826  # Tasa de interés anual del 5%
num_anios = 30
num_veces_acumulacion = 12

# Calcular el valor futuro
tasa_interes_mensual = tasa_interes_anual / num_veces_acumulacion
num_meses = num_anios * num_veces_acumulacion
valor_futuro = aportacion_mensual * (((1 + tasa_interes_mensual) ** num_meses - 1) / tasa_interes_mensual)

# Imprimir el resultado
print(f"El valor futuro es: {valor_futuro:.2f} euros")


