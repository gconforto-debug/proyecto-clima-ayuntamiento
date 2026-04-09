import registro
import validacion
import alertas
import datos_csv

def menu_principal():
    while True:
        print("\n" + "="*30)
        print("🏛️  SISTEMA CLIMÁTICO MUNICIPAL")
        print("="*30)
        print("1. 📝 Registrar nuevos datos")
        print("2. 🔍 Consultar datos por zona")
        print("3. ❌ Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            # 1. Captura
            nuevo_dato = registro.capturar_datos()
            if nuevo_dato is None: continue

            # 2. Validación
            errores = validacion.validar_registro(nuevo_dato)
            if errores:
                print("\n❌ ERROR DE VALIDACIÓN:")
                for e in errores:
                    print(f"   - {e}")
                continue

            # 3. Alertas (Solo si es válido)
            alertas.evaluar_alertas(nuevo_dato)

            # 4. Guardado (Incluye chequeo de duplicados interno)
            datos_csv.guardar_en_csv(nuevo_dato)

        elif opcion == "2":
            zona = input("\n¿Qué zona desea consultar (Centro, Norte, Sur, Este, Oeste)? ").title()
            resultados = datos_csv.consultar_por_zona(zona)

            if not resultados:
                print(f"\n⚠️ No se encontraron registros para la zona: {zona}")
            else:
                print(f"\n--- 📊 LISTADO DE DATOS: {zona.upper()} ---")
                print(f"{'FECHA':<12} | {'TEMP':<6} | {'HUM':<6} | {'VIENTO':<6}")
                print("-" * 45)
                for r in resultados:
                    print(f"{r['fecha']:<12} | {r['temperatura']:<6}ºC | {r['humedad']:<6}% | {r['viento']:<6}km/h")

        elif opcion == "3":
            print("\nCerrando sistema... ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()