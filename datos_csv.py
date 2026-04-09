import csv
import os

# Configuraciones fijas del proyecto
ARCHIVO = "clima_dataset.csv"
COLUMNAS = ["fecha", "zona", "temperatura", "humedad", "viento"]

def registro_existe(fecha, zona):
    """
    Busca si ya existe una fila con la misma fecha y zona para evitar duplicados. 
    """
    if not os.path.exists(ARCHIVO):
        return False
    
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Comparamos los datos del archivo con los que queremos introducir
                if fila["fecha"] == fecha and fila["zona"] == zona:
                    return True
        return False
    except Exception:
        # Si el archivo está corrupto o no se puede leer, asumimos que no hay duplicados
        # para que el programa no se detenga. 
        return False

def guardar_en_csv(registro_dict):
    """
    Recibe un diccionario con los datos y los guarda en el CSV.
    """
    # 1. Verificamos duplicados primero (Calidad de datos) 
    if registro_existe(registro_dict["fecha"], registro_dict["zona"]):
        print(f"\n⚠️ ERROR: Ya existe un registro para la zona '{registro_dict['zona']}' en la fecha {registro_dict['fecha']}.")
        return False

    # 2. Vemos si el archivo ya existe para saber si poner cabeceras (títulos)
    archivo_nuevo = not os.path.exists(ARCHIVO)
    
    try:
        # Abrimos en modo 'a' (append) para añadir al final sin borrar nada 
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=COLUMNAS)
            
            # Si el archivo es nuevo, escribimos los nombres de las columnas arriba
            if archivo_nuevo:
                escritor.writeheader()
            
            # Escribimos los datos reales [cite: 37]
            escritor.writerow(registro_dict)
            
        print("\n✅ Datos digitalizados y guardados con éxito.")
        return True

    except PermissionError:
        print("\n❌ ERROR: No se pudo guardar. Cierra el archivo CSV si lo tienes abierto en Excel.")
        return False
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado al guardar: {e}")
        return False
    
def consultar_por_zona(zona_buscada):
    """
    NUEVA FUNCIÓN: Filtra los datos del CSV por zona geográfica.
    """
    resultados = []
    if not os.path.exists(ARCHIVO):
        return resultados

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Normalizamos la zona para que la búsqueda sea efectiva
                if fila["zona"].strip().title() == zona_buscada.strip().title():
                    resultados.append(fila)
        return resultados
    except Exception as e:
        print(f"❌ Error al consultar los datos: {e}")
        return []