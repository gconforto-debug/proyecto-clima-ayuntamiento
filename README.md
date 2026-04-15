<p align="center" style="margin-bottom: 0px;">
  <img src="docs/skycast_logo_transparent.png" alt="SkyCast Logo" width="350">
</p>

<h1 align="center" style="margin-top: -30px; color: white;">🌧️ SkyCast - Sistema Integral de Gestión de Alertas Municipales</h1>

<p align="center">
  Una plataforma robusta para la monitorización climática urbana y la emisión proactiva de alertas de seguridad ciudadana.
</p>

<<<<<<< HEAD
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Pytest-Tests-green?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Web%20App-Dynamic%20UI-red?style=for-the-badge&logo=html5&logoColor=white" alt="Web App">
  <img src="https://img.shields.io/badge/Git-Version%20Control-black?style=for-the-badge&logo=git&logoColor=white" alt="Git">
</p>
=======
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
-  **Persistencia Inteligente**: Configuración de archivos `.gitattributes` para gestionar estrategias de unión (`merge`) personalizadas. Esto garantiza la integridad de los archivos CSV, evitando que se corrompan al fusionar ramas con diferentes datos.
- **Robustez de Procesamiento**: Implementación de filtros de limpieza de datos y manejo de excepciones, asegurando que la aplicación sea estable incluso ante archivos con formatos inconsistentes.
>>>>>>> a0651b724322904e50b260afcb540169be4be13d

---

## ✨ Introducción a SkyCast

<<<<<<< HEAD
**SkyCast** es una solución integral y fiable diseñada para la monitorización climática y la gestión de riesgos en entornos urbanos. Desarrollado en Python, este sistema robusto permite a las administraciones municipales procesar datos ambientales en tiempo real, generar alertas precisas y proporcionar información valiosa para la toma de decisiones. Su objetivo principal es mejorar la seguridad ciudadana y optimizar la gestión de recursos frente a fenómenos meteorológicos adversos.
=======
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

>>>>>>> a0651b724322904e50b260afcb540169be4be13d

---

## 🚀 Funcionalidades Principales

SkyCast ofrece un conjunto de características clave para una gestión climática municipal eficiente:

- **Monitorización Climática en Tiempo Real:** Captura y procesamiento continuo de datos ambientales como temperatura, humedad y velocidad del viento.
- **Sistema de Alertas Inteligente:** Detección automática y priorizada de situaciones de riesgo crítico (ej. calor extremo, heladas, rachas de viento peligrosas, humedad extrema). La lógica de exclusión en `alertas.py` garantiza que solo se emita la alerta más relevante por categoría.
- **Gestión de Datos Robusta:** Persistencia segura y eficiente de los registros climáticos en formato CSV, con control de duplicados y manejo de errores de permisos.
- **Análisis y Estadísticas Avanzadas:** Generación de informes estadísticos detallados por zona geográfica, proporcionando insights valiosos para la planificación.
- **Control de Acceso Seguro:** Sistema de autenticación de usuarios para garantizar la integridad y privacidad del sistema.
- **Interfaz de Usuario Dual:** Acceso a través de una interfaz de línea de comandos (CLI) y una moderna Interfaz de Visualización Dinámica basada en web.

---

## 🛠️ Arquitectura del Sistema

El proyecto SkyCast se adhiere al principio de **Responsabilidad Única**, estructurando el código en módulos independientes para facilitar el mantenimiento, la escalabilidad y la comprensión.

### Componentes del Backend (Core Lógico)

- **`main.py`**: Punto de entrada principal y orquestador del flujo de la aplicación CLI.
- **`registro.py`**: Módulo encargado de la captura de datos climáticos desde la entrada del usuario.
- **`validacion.py`**: Motor de reglas que asegura la calidad e integridad de los datos, validando formatos y rangos.
- **`alertas.py`**: Módulo central que evalúa los datos climáticos contra umbrales predefinidos para generar alertas de seguridad. Su lógica de exclusión garantiza la emisión de la alerta más severa.
- **`datos_csv.py`**: Implementado con la clase `GestorDatosClima`, esta capa de abstracción gestiona la persistencia y consulta de datos en el archivo CSV, encapsulando la lógica de acceso a datos.
- **`auth.py`**: Módulo de autenticación y gestión de usuarios, garantizando un control de acceso seguro al sistema.

### Interfaz de Visualización Dinámica (Aplicación Web)

La aplicación web de SkyCast actúa como una **Interfaz de Visualización Dinámica**, integrando el core lógico del backend para ofrecer dashboards interactivos. Esta capa permite una gestión visual intuitiva de la casuística climática, presentando datos y alertas de manera accesible sin depender de una tecnología de frontend fija, lo que facilita su evolución y adaptación futura.

---

## 🛡️ Pilares Técnicos y de Calidad

SkyCast se construye sobre una base sólida de excelencia técnica, seguridad y calidad de software:

### A. Seguridad y Control de Acceso

- **Hashing SHA-256 en `auth.py`**: Las credenciales de usuario son protegidas mediante el algoritmo de hashing SHA-256, asegurando que las contraseñas nunca se almacenen en texto plano. Esto garantiza la integridad y confidencialidad de la información sensible.
- **Módulo `auth.py`**: Proporciona una gestión centralizada de registros e inicios de sesión, incluyendo un prototipo de integración con OAuth para futuras expansiones.
- **Privacidad en Consola**: El uso de `getpass` asegura que las credenciales sean invisibles durante la entrada en la interfaz de línea de comandos.

### B. Calidad de Software y Testing

- **Tests Unitarios con `pytest`**: La suite de pruebas automatizadas en la carpeta `/tests` garantiza la fiabilidad del sistema. Esto incluye la validación de la lógica de exclusión de alertas en `alertas.py`, asegurando que los cambios no introduzcan regresiones y que los umbrales críticos funcionen como se espera.
- **Integración Continua**: Las pruebas automatizadas son un pilar para mantener la estabilidad del sistema a medida que evoluciona.

### C. Análisis de Datos Avanzado

- **Integración de `pandas`**: La librería líder en ciencia de datos se utiliza para el procesamiento y análisis eficiente del historial climático.
- **Implementación OOP**: Migración de funciones aisladas a una arquitectura basada en clases mediante el módulo `datos_csv.py`. La clase `GestorDatosClima` centraliza el manejo del dataset, mejorando el encapsulamiento y facilitando el mantenimiento del código. Genera resúmenes estadísticos que incluyen:
  - 🌡️ Medias de temperatura y humedad.
  - 💨 Detección de rachas máximas de viento.
  - 📊 Conteo de registros para asegurar la representatividad de la muestra.
- **Robustez de Procesamiento**: Implementación de filtros de limpieza de datos y manejo avanzado de excepciones, asegurando que la aplicación sea estable incluso ante archivos con formatos inconsistentes.

### D. Gestión de Configuración y Repositorio

- **Persistencia Inteligente**: Configuración de archivos `.gitattributes` para gestionar estrategias de unión (`merge`) personalizadas, garantizando que los archivos CSV críticos no se corrompan durante la integración de ramas.
- **Uso de `.gitignore`**: Se excluyen los archivos `*.csv` mediante la regla `*.csv` para evitar conflictos de fusión (_merge conflicts_) y asegurar que cada desarrollador trabaje con sus propios datos de prueba.
- **Limpieza de Caché**: Se realizó una limpieza profunda de la caché (`git rm --cached`) para garantizar que el archivo de datos no se suba al repositorio remoto una vez activada la política de ignorado.

---

## 🖥️ Interfaz de Visualización Dinámica (Web)

La aplicación web de SkyCast ofrece una experiencia de usuario intuitiva para la visualización de datos climáticos y la gestión de alertas. A través de dashboards interactivos, los usuarios pueden monitorear las condiciones ambientales, revisar el historial de alertas y acceder a estadísticas clave de manera gráfica y comprensible.

### Aplicación Web (Frontend)

> 🚧 **Nota:** La interfaz de visualización se encuentra actualmente en fase de despliegue y ajustes de UI.

<p align="center">
  <img src="docs/banner_skycast.png" alt="Dashboard SkyCast" width="700">
  <br>
  <em>Prototipo de la visualización interactiva de datos climáticos y alertas.</em>
</p>

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para poner en marcha SkyCast en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/gconforto-debug/proyecto-clima-ayuntamiento.git
   cd SkyCast
   ```

2. **Configurar el entorno virtual:**
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar la aplicación CLI:**
   ```bash
   python main.py
   ```

6. **Ejecutar la Aplicación Web:**
   ```bash
   streamlit run app_web.py
   ```

7. **(Opcional) Ejecutar tests unitarios:**
   ```bash
   pytest
   ```

---

## 👥 Equipo de Desarrollo

Este proyecto ha sido desarrollado con la dedicación y el talento de:

- **Gema Villanueva Breña**
- **Gianmario Conforto**
- **Isabela Téllez**
- **Yohanna S. Pérez**
- **Juan de la Fuente Larrocca**
