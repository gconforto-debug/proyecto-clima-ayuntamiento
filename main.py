import registro
import validacion
import alertas
from datos_csv import GestorDatosClima
import auth

def menu_principal():
    # 1. Se instancia el gestor (Nivel Avanzado - OOP)
    gestor = GestorDatosClima()
    
    while True:
        print("\n" + "="*30)
        print("🏛️  SISTEMA CLIMÁTICO MUNICIPAL")
        print("="*30)
        print("1. 📝 Registrar nuevos datos")
        print("2. 🔍 Consultar datos por zona")
        print("3. 📊 Ver Estadísticas (Nivel Medio)") # Nueva opción
        print("4. ❌ Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nuevo_dato = registro.capturar_datos()
            if nuevo_dato is None: continue

            errores = validacion.validar_registro(nuevo_dato)
            if errores:
                print("\n❌ ERROR DE VALIDACIÓN:")
                for e in errores:
                    print(f"   - {e}")
                continue

            alertas.evaluar_alertas(nuevo_dato)

            # 2. Uso del método de la clase
            gestor.guardar_en_csv(nuevo_dato)

        elif opcion == "2":
            ##Definición zonas permitidas
            zonas_validas = ["Norte", "Sur", "Centro", "Este", "Oeste"]

            print("\n--- 🔍 Consulta de Registros ---")
            print(f"Zonas disponibles: {', '.join(zonas_validas)}")

            zona = input("\n¿Qué zona desea consultar? ").title()
            
            #Validación por zona
            if zona not in zonas_validas:
                print(f"\n ❌ ERROR: La zona '{zona}' no es válida.")
                print(f" Solo puede consultar: {', '.join(zonas_validas)}")
            else:
                # 3. Uso del método de la clase
                resultados = gestor.consultar_por_zona(zona)

                if not resultados:
                    print(f"\n⚠️ No se encontraron registros para la zona: {zona}")
                else:
                    print(f"\n--- 📋 LISTADO DE DATOS: {zona.upper()} ---")
                    print(f"{'FECHA':<12} | {'TEMP':<6} | {'HUM':<6} | {'VIENTO':<6}")
                    print("-" * 45)
                    
                # Como ahora devuelve un DataFrame o lista, iteramos:
                for r in resultados:
                    print(f"{r['fecha']:<12} | {r['temperatura']:<6}ºC | {r['humedad']:<6}% | {r['viento']:<6}km/h")

        elif opcion == "3":
            # 4. NUEVA FUNCIONALIDAD: Estadísticas
            ##Definición zonas permitidas
            zonas_validas = ["Norte", "Sur", "Centro", "Este", "Oeste"]

            print("\n--- 📊 Módulo de Análisis Estadístico ---")
            print(f"Zonas disponibles: {', '.join(zonas_validas)}")

            zona = input("Escriba la zona a consultar: ").strip().title()

            ##Validar si la zona escrit está en la listas
            if zona not in zonas_validas:
                print(f"\n ❌ ERROR: La zona '{zona}' no es válida.")
                print(f" Solo puede consultar: {', '.join(zonas_validas)}")
            else:
                ###Si es válida se procede al gestor
                stats = gestor.obtener_estadisticas_zona(zona)
            
                if stats:
                    print(f"\n--- 📊 RESUMEN ESTADÍSTICO: {zona.upper()} ---")
                    print(f"✅ Mediciones totales: {stats['conteo']}")
                    print(f"🌡️ Temperatura Media: {stats['media_temp']:.2f}ºC")
                    print(f"🔥 Temp. Máxima:      {stats['max_temp']}ºC")
                    print(f"💧 Humedad Media:     {stats['media_hum']:.1f}%")
                    print(f"💨 Viento Máximo:     {stats['max_viento']} km/h")
                else:
                    print(f"\n⚠️ No hay datos suficientes para generar estadísticas en {zona}.")

        elif opcion == "4":
            print("\nCerrando sistema... ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción no válida. Intente de nuevo.")

if _name_ == "_main_":
    if auth.solicitar_acceso():
        menu_principal()