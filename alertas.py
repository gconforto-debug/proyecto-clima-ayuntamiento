# alertas.py

def analizar_riesgos(t, v):
    """
    Recibe temperatura (t) y viento (v). 
    Imprime avisos si se superan los umbrales del Ayuntamiento.
    """
    # Alerta por Calor Extremo
    if t >= 40:
        print("⚠️  [ALERTA CALOR] Protocolo de emergencia activo. Evitar actividades al aire libre.")
    
    # Alerta por Frío/Heladas (Extra para nota)
    elif t <= 0:
        print("❄️  [ALERTA HELADA] Riesgo de placas de hielo en pavimentos.")

    # Alerta por Viento Fuerte
    if v >= 80:
        print("💨 [ALERTA VIENTO] Riesgo de caída de ramas. Cierre preventivo de parques.")

    # Si todo está bien, podrías añadir un mensaje opcional
    if 0 < t < 40 and v < 80:
        print("✅ Parámetros climáticos dentro de la normalidad.")