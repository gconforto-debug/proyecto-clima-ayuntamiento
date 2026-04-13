<p align="center">
  <img src="docs/skycast_logo_transparent.png" alt="SkyCast Logo" width="220">
</p>

# 🌦️ SkyCast - MVP Sprint 1

**SkyCast** (Sistema de Gestión de Alertas Municipales) es una solución modular desarrollada en Python para la monitorización climática urbana. Este sistema permite a los técnicos municipales registrar datos precisos, validar su integridad en tiempo real y emitir alertas automáticas basadas en umbrales de seguridad ciudadana establecidos por la AEMET.

## 🚀 Funcionalidades del Sprint 1

En esta primera fase, nos hemos centrado en la estabilidad del núcleo y la persistencia de datos:

- **Interfaz de Comandos (CLI):** Menú interactivo robusto con control de errores de navegación.
- **Registro Validado:** Sistema de entrada que impide datos incoherentes (fechas inexistentes, temperaturas fuera de rango lógico de -20ºC a 60ºC o zonas no autorizadas).
- **Motor de Alertas Inteligente:** Lógica de negocio que prioriza avisos de seguridad (Calor Extremo, Heladas, Rachas de Viento) antes de confirmar el guardado.
- **Persistencia Profesional (CSV):** Gestión de datos en formato plano con control de duplicados (evita registrar la misma zona dos veces en un mismo día) y manejo de errores de permisos.
- **Consulta por Filtros:** Motor de búsqueda con normalización de texto (`.strip()` y `.title()`) para garantizar resultados precisos independientemente de cómo escriba el usuario.

## 🛠️ Arquitectura Modular

El proyecto sigue el principio de **Responsabilidad Única**, dividiendo el código en módulos independientes para facilitar el mantenimiento y el escalado:

1.  **`main.py`**: Punto de entrada y gestión del flujo del usuario (Menú principal).
2.  **`registro.py`**: Coordinador de captura y orquestación de procesos entre entrada, validación y alertas.
3.  **`validacion.py`**: Motor de reglas lógicas que asegura la calidad de los datos (fechas y rangos físicos).
4.  **`alertas.py`**: Configurador de umbrales críticos y generación de avisos visuales inmediatos.
5.  **`datos_csv.py`**: Capa de acceso a datos (Lectura/Escritura) y gestión de persistencia física en el dataset.

## 🔧 Instalación y Uso

Sigue estos pasos para poner en marcha el sistema en tu entorno local:

1.  **Clonar el repositorio:** `git clone [URL_DEL_REPOSITORIO]`
2.  **Configurar el entorno virtual:** `python -m venv .venv`
3.  **Activar el entorno:** \* Windows: `.venv\Scripts\activate`
    - Linux/Mac: `source .venv/bin/activate`
4.  **Instalar dependencias necesarias:** `pip install -r requirements.txt`
5.  **Ejecutar la aplicación:** `python main.py`
6.  **(Opcional) Ejecutar tests unitarios:** `pytest`

## 📦 Gestión de Git y Colaboración

Se ha implementado una política de **"Código Global, Datos Locales"**:

- **Uso de `.gitignore`:** Se excluyen los archivos `*.csv` mediante la regla `*.csv` para evitar conflictos de fusión (_merge conflicts_) y asegurar que cada desarrollador trabaje con sus propios datos de prueba.
- **Limpieza de Caché:** Se realizó una limpieza profunda de la caché (`git rm --cached`) para garantizar que el archivo de datos no se suba al repositorio remoto una vez activado el ignore.

---

## ⏭️ Próximas Mejoras (Roadmap Sprint 2)

Tras consolidar la base del sistema, las siguientes actualizaciones se centrarán en el análisis avanzado y la experiencia de usuario:

---

_Este proyecto ha sido desarrollado como parte del Sprint 1 para demostrar competencias en Python modular, manejo de archivos, validación de datos y control de versiones con Git._
