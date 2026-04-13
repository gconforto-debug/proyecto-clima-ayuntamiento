from datetime import datetime


def validar_registro(registro):
    """
    Valida un registro climático recibido en forma de diccionario.

    Parámetro:
        registro (dict): Diccionario con las claves:
            - fecha
            - zona
            - temperatura
            - humedad
            - viento

    Devuelve:
        list: Lista de errores encontrados.
        Si la lista está vacía, el registro es válido.
    """

    errores = []
    zonas_validas = ["Centro", "Norte", "Sur", "Este", "Oeste"]

    fecha = str(registro.get("fecha", "")).strip()
    zona = str(registro.get("zona", "")).strip().title()
    temperatura = registro.get("temperatura")
    humedad = registro.get("humedad")
    viento = registro.get("viento")

    # VALIDACIÓN DE FECHA
    if fecha == "":
        errores.append("Fecha vacía")
    else:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            errores.append("Fecha incorrecta (formato o no existe)")

    # VALIDACIÓN DE ZONA
    if zona == "":
        errores.append("Zona vacía")
    elif zona not in zonas_validas:
        errores.append("Zona no válida")

    # VALIDACIÓN DE TEMPERATURA
    try:
        temperatura = float(temperatura)
        if temperatura < -20 or temperatura > 60:
            errores.append("Temperatura fuera de rango (-20 a 60)")
    except (TypeError, ValueError):
        errores.append("Temperatura no válida")

    # VALIDACIÓN DE HUMEDAD
    try:
        humedad = float(humedad)
        if humedad < 0 or humedad > 100:
            errores.append("Humedad fuera de rango (0 a 100)")
    except (TypeError, ValueError):
        errores.append("Humedad no válida")

    # VALIDACIÓN DE VIENTO
    try:
        viento = float(viento)
        if viento < 0 or viento > 150:
            errores.append("Viento fuera de rango (0 a 150)")
    except (TypeError, ValueError):
        errores.append("Viento no válido")

    return errores