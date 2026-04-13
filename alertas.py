# alertas.py

# Mantenemos la configuración, pero la lógica ahora será más inteligente
ALERTAS_CONFIG = {
    'calor_roja':    {'campo': 'temperatura', 'umbral': 40, 'msj': '🔴 ALERTA ROJA: Calor extremo (≥40ºC). Protocolo activado.'},
    'calor_naranja': {'campo': 'temperatura', 'umbral': 35, 'msj': '🟠 ALERTA NARANJA: Calor alto (≥35ºC). Precaución.'},
    'viento_fuerte': {'campo': 'viento',      'umbral': 70, 'msj': '💨 ALERTA VIENTO: Riesgo por rachas fuertes (>70 km/h).'},
    'humedad_ext':   {'campo': 'humedad',     'umbral': 90, 'msj': '💧 ALERTA HUMEDAD: Humedad extrema (≥90%).'},
    'hielo':         {'campo': 'temperatura', 'umbral': 0,  'msj': '❄️ AVISO HELADA: Riesgo de placas de hielo.', 'tipo': 'frio'}
}

def evaluar_alertas(registro):
    """
    Analiza un diccionario de registro y detecta situaciones de riesgo.
    Filtra alertas duplicadas para mostrar solo la más severa por categoría.
    """
    alertas_detectadas = []
    
    try:
        # Convertimos a float de forma segura
        temp = float(registro.get('temperatura', 0))
        viento = float(registro.get('viento', 0))
        humedad = float(registro.get('humedad', 0))

        # --- 1. LÓGICA DE TEMPERATURA (Prioridad) ---
        # El uso de if/elif asegura que solo se dispare UNA de estas tres
        if temp >= ALERTAS_CONFIG['calor_roja']['umbral']:
            alertas_detectadas.append(ALERTAS_CONFIG['calor_roja']['msj'])
        elif temp >= ALERTAS_CONFIG['calor_naranja']['umbral']:
            alertas_detectadas.append(ALERTAS_CONFIG['calor_naranja']['msj'])
        elif temp <= ALERTAS_CONFIG['hielo']['umbral']:
            alertas_detectadas.append(ALERTAS_CONFIG['hielo']['msj'])

        # --- 2. LÓGICA DE VIENTO ---
        if viento >= ALERTAS_CONFIG['viento_fuerte']['umbral']:
            alertas_detectadas.append(ALERTAS_CONFIG['viento_fuerte']['msj'])

        # --- 3. LÓGICA DE HUMEDAD ---
        if humedad >= ALERTAS_CONFIG['humedad_ext']['umbral']:
            alertas_detectadas.append(ALERTAS_CONFIG['humedad_ext']['msj'])

    except (ValueError, TypeError):
        print("❌ Error: Los datos climáticos para alertas deben ser numéricos.")
        return []

    # Salida por consola (Integración con el flujo de main.py)
    if alertas_detectadas:
        print("\n🚨 ALERTAS DETECTADAS:")
        for msj in alertas_detectadas:
            print(f"   {msj}")
            
    return alertas_detectadas