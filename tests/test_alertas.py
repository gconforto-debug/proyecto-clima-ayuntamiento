# test_alertas.py
from alertas import evaluar_alertas

def test_alerta_calor_extremo():
    """Valida la detección de calor extremo >= 40ºC"""
    datos = {'temperatura': 42.5, 'viento': 10, 'humedad': 30}
    resultado = evaluar_alertas(datos)
    assert any("ALERTA ROJA" in s for s in resultado)

def test_alerta_viento_fuerte():
    """Valida la detección de viento fuerte >= 90 km/h"""
    datos = {'temperatura': 20, 'viento': 90, 'humedad': 50}
    resultado = evaluar_alertas(datos)
    assert any("VIENTO" in s for s in resultado)

def test_alerta_temperatura_extrema():
    """Valida la detección de calor extremo para temperaturas muy altas"""
    datos = {'temperatura': 100, 'viento': 10, 'humedad': 30}
    resultado = evaluar_alertas(datos)
    assert any("ALERTA ROJA" in s for s in resultado)

def test_alerta_humedad_extrema():
    """Valida la detección de humedad extrema >= 90%"""
    datos = {'temperatura': 15, 'viento': 5, 'humedad': 95}
    resultado = evaluar_alertas(datos)
    assert any("HUMEDAD" in s for s in resultado)

def test_datos_invalidos():
    """Asegura que el programa maneje correctamente datos erróneos"""
    datos = {'temperatura': "Mucho calor", 'viento': 10, 'humedad': 30}
    # La función debe imprimir el error y retornar una lista vacía para no romper el flujo
    resultado = evaluar_alertas(datos)
    assert resultado == []

if __name__ == "__main__":
    print("🧪 Ejecutando suite de pruebas locales para evaluar_alertas...")
    try:
        test_alerta_calor_extremo()
        test_alerta_viento_fuerte()
        test_alerta_temperatura_extrema()
        test_alerta_humedad_extrema()
        test_datos_invalidos()
        print("\n¡Pruebas superadas con éxito! ✅")
    except AssertionError as e:
        print(f"\n❌ Error en los tests: {e}")