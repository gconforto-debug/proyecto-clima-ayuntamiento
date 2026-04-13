import pytest
import os
# Importamos directamente porque 'python -m' se encarga de encontrarlos
from datos_csv import guardar_en_csv, ARCHIVO

def test_escritura_archivo():
    """Prueba que el archivo se crea y guarda datos."""
    # 1. Preparación: Limpiamos si existe un archivo de pruebas previo
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
    
    # 2. Datos de prueba
    registro = {
        "fecha": "2026-04-08", 
        "zona": "Test", 
        "temperatura": 20, 
        "humedad": 50, 
        "viento": 10
    }
    
    # 3. Ejecución
    guardar_en_csv(registro)
    
    # 4. Verificación (Los "assert" son las preguntas del examen)
    assert os.path.exists(ARCHIVO) == True
    assert os.path.getsize(ARCHIVO) > 0