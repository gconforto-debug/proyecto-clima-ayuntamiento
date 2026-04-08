# alertas.py

# Configuración de umbrales según el MVP y la guía técnica de DashLogistics
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
    Compatible con la llamada en main.py de Gianmario.
    """
    alertas_detectadas = []
    
    try:
        for clave, conf in ALERTAS_CONFIG.items():
            # Extraemos el valor usando la llave definida en la configuración
            valor_sensor = registro.get(conf['campo'])
            
            if valor_sensor is None:
                continue
                
            valor = float(valor_sensor)
            
            # Lógica para frío (<=) y calor/viento/humedad (>=)
            if conf.get('tipo') == 'frio':
                if valor <= conf['umbral']:
                    alertas_detectadas.append(conf['msj'])
            else:
                if valor >= conf['umbral']:
                    alertas_detectadas.append(conf['msj'])

    except (ValueError, TypeError):
        print("❌ Error: Los datos climáticos para alertas deben ser numéricos.")
        return []

    # Salida por consola directa (Integración con el flujo de main.py)
    if alertas_detectadas:
        print("\n🚨 ALERTAS DETECTADAS:")
        for msj in alertas_detectadas:
            print(f"   {msj}")
            
    return alertas_detectadas