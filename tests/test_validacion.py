import validacion

def test_temperatura_fuera_de_rango():
    # Creamos un registro falso con temperatura loca
    registro_mal = {
        "fecha": "2026-04-13",
        "zona": "Norte",
        "temperatura": 500, # ¡Imposible!
        "humedad": 50,
        "viento": 10
    }
    errores = validacion.validar_registro(registro_mal)
    assert "Temperatura fuera de rango (-20 a 60)" in errores

def test_fecha_incorrecta():
    registro_mal = {
        "fecha": "2026-13-40", # Mes 13 no existe
        "zona": "Norte",
        "temperatura": 20,
        "humedad": 50,
        "viento": 10
    }
    errores = validacion.validar_registro(registro_mal)
    assert "Fecha incorrecta (formato o no existe)" in errores