# test_alertas.py
from alertas import analizar_riesgos

def test_alerta_calor_extremo():
    # Si hace 45 grados, debería haber una alerta de calor
    resultado = analizar_riesgos(45, 10)
    assert any("CALOR" in s for s in resultado)

def test_alerta_viento_fuerte():
    # Si el viento es de 90 km/h, debería haber alerta de viento
    resultado = analizar_riesgos(20, 90)
    assert any("VIENTO" in s for s in resultado)

print("¡Pruebas superadas con éxito! ✅")