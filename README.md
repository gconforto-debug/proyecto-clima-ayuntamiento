<p align="center" style="margin-bottom: 0px;">
  <img src="docs/skycast_logo_transparent.png" alt="SkyCast Logo" width="350">
</p>

<h1 align="center" style="margin-top: -30px; color: white;">🌧️ SkyCast - MVP Sprint 1</h1>

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

## 📈 Evolución y Mejoras Continuas

Tras completar el **Sprint 1**, seguimos trabajando en el proyecto para hacerlo más seguro y profesional. Nuestro objetivo es mejorar la experiencia del usuario y fortalecer el código para que sea más robusto antes de la entrega final.

A continuación, se detallan las funcionalidades que ya han sido integradas con éxito y las líneas de mejora que iremos implementando de cara a la entrega final:

### **🛡️ Seguridad y Control de Acceso (Implementado)**

Hemos blindado la aplicación con un sistema de gestión de identidades robusto:

- **Módulo `auth.py`**: Gestión centralizada de registros e inicios de sesión.
- **Hashing SHA-256**: Las contraseñas se procesan mediante algoritmos criptográficos, asegurando que solo se almacenen huellas digitales y nunca texto plano.
- **Privacidad en Consola**: Uso de `getpass` para que las credenciales sean invisibles durante la escritura.
- **Acceso Dual**: Capacidad de login tradicional y prototipo de integración con Google (OAuth).

### **🧪 Calidad de Software (Implementado)**

- **Tests Unitarios**: Integración de la carpeta `/tests` con pruebas automatizadas mediante `pytest`. Esto garantiza que cualquier cambio en la lógica de alertas o validación no rompa el sistema (Integración Continua).

### **📈 Arquitectura Avanzada y Análisis de Datos (Implementado)**

Hemos elevado el nivel técnico del proyecto integrando herramientas de análisis profesional y un diseño de software basado en estándares industriales:

- **Implementación OOP**: Migración de funciones aisladas a una arquitectura basada en clases mediante el módulo `datos_csv.py`. La clase `GestorDatosClima` centraliza el manejo del dataset, mejorando el encapsulamiento y facilitando el mantenimiento del código.
- **Análisis con Pandas**: Integración de la librería líder en ciencia de datos para procesar el historial climático. El sistema ahora genera resúmenes estadísticos automáticos por zona que incluyen:
    - 🌡️ Medias de temperatura y humedad.
    - 💨 Detección de rachas máximas de viento.
    - 📊 Conteo de registros para asegurar la representatividad de la muestra.
- **Persistencia Inteligente**: Configuración de archivos `.gitattributes` para gestionar estrategias de unión (`merge`) personalizadas. Esto garantiza la integridad de los archivos CSV, evitando que se corrompan al fusionar ramas con diferentes datos.
- **Robustez de Procesamiento**: Implementación de filtros de limpieza de datos y manejo de excepciones, asegurando que la aplicación sea estable incluso ante archivos con formatos inconsistentes.

---

_Este proyecto ha sido desarrollado como parte del Sprint 1 para demostrar competencias en Python modular, manejo de archivos, validación de datos y control de versiones con Git._
