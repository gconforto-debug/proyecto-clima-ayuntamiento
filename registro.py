def capturar_datos():
    """
    EL RECEPCIONISTA: Pide los datos por consola y los devuelve en un diccionario organizado.
    """
    print("\n--- 📝 NUEVO REGISTRO CLIMÁTICO ---")

    # 1. CAPTURA DE TEXTO
    fecha = input("Fecha (AAAA-MM-DD): ")
    zona = input("Zona de la ciudad (Norte, Sur, Centro,Este, Oeste): ")

    # 2. CAPTURA Y CONVERSIÓN NUMÉRICA
    try:
        # Se usan los nombres de variables definidas por el equipo
        temperatura = float(input("Temperatura (°C): ")) 
        humedad = float(input("Humedad (%): "))
        viento = float(input("Viento (km/h): "))

        # 3. EMPAQUETADO: Las variables coinciden con las llaves
        nuevo_registro = {
            "fecha": fecha,
            "zona": zona,
            "temperatura": temperatura,
            "humedad": humedad,
            "viento": viento
        }

        return nuevo_registro

    except ValueError:
        print("\n❌ ERROR: Temperatura, Humedad y Viento deben ser números.")
        return None