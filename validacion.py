import csv  # Importamos csv para poder leer el archivo CSV con los registros de climas
from datetime import datetime  # Importamos datetime para poder validar fechas


def validar_registro(registro):  # Definimos una función que recibe UN registro (un diccionario)

    errores = []  # Creamos una lista vacía donde guardaremos los errores encontrados

    # Lista de zonas válidas permitidas
    zonas_validas = ["Centro", "Norte", "Sur", "Este", "Oeste"]

    # Sacamos los valores del registro para trabajar más cómodo
    fecha = registro["fecha"]
    zona = registro["zona"]
    temperatura = registro["temperatura"]
    humedad = registro["humedad"]
    viento = registro["viento"]

    # -------------------
    # VALIDACIÓN DE FECHA
    # -------------------

    if fecha == "":  # Si la fecha está vacía
        errores.append("Fecha vacía")  # Añadimos error a la lista
    else:
        try:
            # Intentamos convertir la fecha al formato YYYY-MM-DD
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            # Si falla, significa que el formato es incorrecto o la fecha no existe
            errores.append("Fecha incorrecta (formato o no existe)")

    # -------------------
    # VALIDACIÓN DE ZONA
    # -------------------

    if zona == "":  # Si la zona está vacía
        errores.append("Zona vacía")
    elif zona not in zonas_validas:  # Si no está en la lista de zonas válidas
        errores.append("Zona no válida")

    # ---------------------------
    # VALIDACIÓN DE TEMPERATURA
    # ---------------------------

    # Comprobamos si está fuera del rango permitido
    if temperatura < -20 or temperatura > 60:
        errores.append("Temperatura fuera de rango (-20 a 60)")

    # -----------------------
    # VALIDACIÓN DE HUMEDAD
    # -----------------------

    if humedad < 0 or humedad > 100:  # Rango válido de humedad
        errores.append("Humedad fuera de rango (0 a 100)")

    # ----------------------
    # VALIDACIÓN DE VIENTO
    # ----------------------

    if viento < 0 or viento > 150:  # Rango válido de viento
        errores.append("Viento fuera de rango (0 a 150)")

    # -------------------
    # RESULTADO FINAL
    # -------------------

    return errores  # Devolvemos la lista de errores (vacía si todo está bien)