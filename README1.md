# 🌦️ App Climática — Ayuntamiento

> Sistema de monitorización climática con alertas tempranas para la gestión municipal del riesgo meteorológico.  
> Proyecto de bootcamp · SomosF5 / AI4Inclusion · 2025-2026

---

## 📋 Índice

- [Descripción](#descripción)
- [Arquitectura del proyecto](#arquitectura-del-proyecto)
- [Tablero Kanban](#tablero-kanban)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Tecnologías](#tecnologías)
- [Referencias](#referencias)

---

## Descripción

Aplicación Python para el **Ayuntamiento de Valencia** que permite:

- Cargar y procesar datos climáticos históricos desde CSV
- Validar la integridad y coherencia de los registros
- Registrar nuevas lecturas de sensores IoT
- Detectar condiciones meteorológicas extremas y emitir alertas tempranas
- Orquestar el flujo completo desde `main.py`

Fundamentado en literatura científica: **Satpathy et al. (2025)** — *AI for Climate Change and Environmental Sustainability* — que avala el uso de sensores IoT, modelos Random Forest y Sistemas de Alerta Temprana (EWS) en gestión climática municipal.

---

## Arquitectura del proyecto

```
proyecto-clima-ayuntamiento/
│
├── main.py              # Orquestador principal del flujo
├── datos_csv.py         # Carga y procesamiento del dataset CSV
├── validacion.py        # Validación de integridad de datos
├── registro.py          # Registro de nuevas lecturas de sensores
├── alertas.py           # Motor de alertas climáticas tempranas
│
├── clima_dataset.csv    # Dataset histórico de registros climáticos
├── requirements.txt     # Dependencias del proyecto (pytest>=8.0.0)
├── .gitignore
└── README.md
```

---

## Tablero Kanban

El desarrollo del proyecto sigue metodología **Kanban** con cinco columnas de estado. Cada tarjeta corresponde a una tarea concreta del sprint.

---

### 📥 BACKLOG — Tareas pendientes de planificación

| # | Tarea | Archivo asociado |
|---|-------|-----------------|
| B-01 | Definir estructura del dataset climático (columnas, tipos, rangos) | `clima_dataset.csv` |
| B-02 | Investigar umbrales oficiales AEMET para alertas por temperatura, lluvia y viento | `alertas.py` |
| B-03 | Diseñar esquema de validación de entradas del sensor IoT | `validacion.py` |
| B-04 | Documentar casos de uso del sistema para el Ayuntamiento | `README.md` |
| B-05 | Definir formato de salida del registro de lecturas | `registro.py` |

---

### 🔵 TODO — Listo para empezar

| # | Tarea | Archivo asociado |
|---|-------|-----------------|
| T-01 | Implementar `cargar_datos()` — lectura del CSV con pandas | `datos_csv.py` |
| T-02 | Implementar `validar_registro()` — comprobación de tipos y valores nulos | `validacion.py` |
| T-03 | Implementar `registrar_lectura()` — añadir fila al CSV con timestamp | `registro.py` |
| T-04 | Implementar `generar_alerta()` — lógica de detección de eventos extremos | `alertas.py` |
| T-05 | Escribir `main.py` — orquestación del flujo completo E2E | `main.py` |

---

### 🟡 IN PROGRESS — En desarrollo activo

| # | Tarea | Responsable | Archivo asociado |
|---|-------|-------------|-----------------|
| IP-01 | Crear dataset `clima_dataset.csv` con datos de prueba (Valencia 2024) | equipo | `clima_dataset.csv` |
| IP-02 | Implementar manejo de excepciones en carga CSV (archivo no encontrado, columnas faltantes) | equipo | `datos_csv.py` |
| IP-03 | Escribir tests unitarios para `validacion.py` con pytest | equipo | `validacion.py` |

---

### 🔍 IN REVIEW — En revisión / Pull Request abierto

| # | Tarea | PR | Archivo asociado |
|---|-------|----|-----------------|
| R-01 | Revisión de lógica de umbrales en `alertas.py` (comparativa con normativa AEMET) | #1 | `alertas.py` |
| R-02 | Code review de `registro.py` — verificar que no sobrescribe datos existentes | — | `registro.py` |

---

### ✅ DONE — Completado

| # | Tarea | Fecha | Archivo asociado |
|---|-------|-------|-----------------|
| D-01 | Inicializar repositorio con `.gitignore` y estructura de archivos | Abr 2026 | `.gitignore` |
| D-02 | Crear `requirements.txt` con dependencia `pytest>=8.0.0` | Abr 2026 | `requirements.txt` |
| D-03 | Definir nombres y responsabilidades de los cinco módulos Python | Abr 2026 | todos los `.py` |
| D-04 | Primera versión de `README.md` | Abr 2026 | `README.md` |

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/gconforto-debug/proyecto-clima-ayuntamiento.git
cd proyecto-clima-ayuntamiento

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Uso

```bash
# Ejecutar el flujo principal
python main.py
```

El programa:
1. Carga el dataset climático desde `clima_dataset.csv` (`datos_csv.py`)
2. Valida la integridad de los registros (`validacion.py`)
3. Registra nuevas lecturas si se proporcionan (`registro.py`)
4. Evalúa condiciones extremas y emite alertas si procede (`alertas.py`)

---

## Tests

```bash
# Ejecutar suite de tests
pytest

# Con detalle de cobertura
pytest -v
```

Los tests cubren: validación de tipos, detección de valores fuera de rango, manejo de registros vacíos y lógica de umbrales de alerta.

---

## Tecnologías

| Herramienta | Uso |
|-------------|-----|
| Python 3.10+ | Lenguaje principal |
| pandas | Procesamiento de datos CSV |
| pytest ≥ 8.0.0 | Testing unitario |
| CSV / IoT data | Fuente de datos climáticos |

---

## Referencias

> Satpathy, S. et al. (2025). *AI for Climate Change and Environmental Sustainability*. Springer.  
> Avala el uso de sensores IoT para monitorización en tiempo real, modelos Random Forest para predicción de eventos extremos y Sistemas de Alerta Temprana (EWS) en gestión climática municipal.

---

## Equipo

Desarrollado en el marco del bootcamp **SomosF5 / AI4Inclusion** — Madrid, 2025-2026.  
Cliente simulado: Ayuntamiento de Valencia · Departamento de Gestión de Riesgos Climáticos.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/pytest-≥8.0.0-green?style=flat-square&logo=pytest" />
  <img src="https://img.shields.io/badge/estado-en%20desarrollo-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/bootcamp-SomosF5-orange?style=flat-square" />
</p>
