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
            fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()
            fecha_hoy = datetime.today().date()   
            if fecha_convertida > fecha_hoy:
                errores.append("Fecha no válida. No se permiten fechas futuras.")
        except ValueError:
            errores.append("Fecha incorrecta. Usa formato YYYY-MM-DD (ej: 2026-11-13) y comprueba que la fecha corresponda al día de hoy.")

    # VALIDACIÓN DE ZONA
    if zona == "":
        errores.append("Zona vacía")
    elif zona not in zonas_validas:
        errores.append(f"Zona no válida. Zonas permitidas: {', '.join(zonas_validas)}")


    # VALIDACIÓN DE TEMPERATURA
    try:
        temperatura = float(temperatura)
        if temperatura < -20 or temperatura > 60:
            errores.append("Temperatura fuera de rango.Introduce un valor entre -20 y 60)")
    except (TypeError, ValueError):
        errores.append("Temperatura no válida")

    # VALIDACIÓN DE HUMEDAD
    try:
        humedad = float(humedad)
        if humedad < 0 or humedad > 100:
            errores.append("Humedad fuera de rango. Introduce un valor entre 0 y 100)")
    except (TypeError, ValueError):
        errores.append("Humedad no válida")

    # VALIDACIÓN DE VIENTO
    try:
        viento = float(viento)
        if viento < 0 or viento > 150:
            errores.append("Viento fuera de rango. Introduce un valor entre 0 y 150km/h)")
    except (TypeError, ValueError):
        errores.append("Viento no válido")

    return errores