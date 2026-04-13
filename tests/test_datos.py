import datos_csv  # Importamos el módulo completo

def test_guardar_registro_clase():
    # 1. Creamos el objeto (instancia) de la clase que hizo tu compañero
    gestor = datos_csv.GestorDatosClima()
    
    # 2. Preparamos un registro de prueba
    registro = {
        "fecha": "2026-04-13",
        "zona": "Norte",
        "temperatura": 25.0,
        "humedad": 60,
        "viento": 15
    }
    
    # 3. Llamamos al método usando el objeto 'gestor'
    resultado = gestor.guardar_en_csv(registro)
    
    # 4. Verificamos que devuelva True
    assert resultado is True