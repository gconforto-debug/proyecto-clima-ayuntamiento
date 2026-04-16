import csv
import os
import pandas as pd # Importante para las estadísticas

class GestorDatosClima:
    def __init__(self):
        # Se mantienen las configuraciones fijas como atributos de clase
        self.ARCHIVO = "clima_dataset.csv"
        self.COLUMNAS = ["fecha", "zona", "temperatura", "humedad", "viento"]

    def registro_existe(self, fecha, zona):
        """Busca si ya existe una fila con la misma fecha y zona."""
        if not os.path.exists(self.ARCHIVO):
            return False
        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    if fila["fecha"] == fecha and fila["zona"] == zona:
                        return True
            return False
        except Exception:
            return False

    def guardar_en_csv(self, registro_dict):
        """Guarda los datos en el CSV con la lógica original."""
        if self.registro_existe(registro_dict["fecha"], registro_dict["zona"]):
            print(f"\n⚠️ ERROR: Ya existe un registro para {registro_dict['zona']} en la fecha {registro_dict['fecha']}.")
            return False

        archivo_nuevo = not os.path.exists(self.ARCHIVO)
        try:
            with open(self.ARCHIVO, "a", newline="", encoding="utf-8") as f:
                escritor = csv.DictWriter(f, fieldnames=self.COLUMNAS)
                if archivo_nuevo:
                    escritor.writeheader()
                escritor.writerow(registro_dict)
            print("\n✅ Datos digitalizados y guardados con éxito.")
            return True
        except PermissionError:
            print("\n❌ ERROR: Cierra el archivo CSV si lo tienes abierto en Excel.")
            return False
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            return False

    def consultar_por_zona(self, zona_buscada):
        """Filtra los datos y los devuelve como una lista (tu función original)."""
        resultados = []
        if not os.path.exists(self.ARCHIVO):
            return resultados
        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    if fila["zona"].strip().title() == zona_buscada.strip().title():
                        resultados.append(fila)
            return resultados
        except Exception as e:
            print(f"❌ Error al consultar: {e}")
            return []
        
    # --- ESTADÍSTICAS (Nivel Medio) ---
    def obtener_estadisticas_zona(self, zona_buscada):
        if not os.path.exists(self.ARCHIVO):
            return None
        
        try:
            # Forzamos a que lea todo como strings primero para evitar errores de tipo
            df = pd.read_csv(self.ARCHIVO, skipinitialspace=True)
            
            # Limpiamos nombres de columnas por si acaso
            df.columns = df.columns.str.strip()
            
            # Filtro robusto
            df_zona = df[df['zona'].str.strip().str.title() == zona_buscada.strip().title()]
            
            if df_zona.empty:
                return None

            return {
                "media_temp": float(df_zona['temperatura'].mean()),
                "max_temp": float(df_zona['temperatura'].max()),
                "min_temp": float(df_zona['temperatura'].min()),
                "media_hum": float(df_zona['humedad'].mean()),
                "max_viento": float(df_zona['viento'].max()),
                "conteo": int(len(df_zona))
            }
        except Exception as e:
            print(f"Error estadístico: {e}")
            return None