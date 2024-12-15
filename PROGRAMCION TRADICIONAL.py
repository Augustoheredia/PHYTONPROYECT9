def ingresar_temperaturas_semanales():
    """
    Pide al usuario que ingrese las temperaturas diarias de una semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = [2]
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el promedio.
    """
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

# Llamado a las funciones
temperaturas_semana = ingresar_temperaturas_semanales()
promedio_semanal = calcular_promedio(temperaturas_semana)

print(f"El promedio de temperatura semanal es: {promedio_semanal:.2f}°C")