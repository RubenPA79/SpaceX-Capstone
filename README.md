# 🚀 Análisis y Predicción de Aterrizajes del Falcon 9 de SpaceX

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Proyecto Capstone de Ciencia de Datos**: Predicción exitosa de la recuperación de la primera etapa del Falcon 9 para optimización de costos en lanzamientos espaciales.

## 📖 Descripción del Proyecto
El objetivo principal es predecir si la primera etapa del cohete Falcon 9 aterrizará con éxito. SpaceX ofrece lanzamientos a precios competitivos ($62M vs $165M de competidores) gracias a la reutilización de la primera etapa. Determinar la probabilidad de aterrizaje permite estimar costos reales y ofertar mejor en el mercado.

Este proyecto abarca el ciclo completo de Data Science: desde la recolección de datos (API/Web Scraping) hasta el despliegue de un Dashboard interactivo y modelos de Machine Learning.

## 📂 Estructura del Proyecto

El repositorio ha sido organizado para garantizar la reproducibilidad y escalabilidad:

```
├── 📂 data/        # Datasets crudos y procesados
├── 📂 database/    # Base de datos SQLite (spacex.db)
├── 📂 notebooks/   # Jupyter Notebooks de exploración y prototipado
├── 📂 reports/     # Presentaciones (PDF/PPTX) y Mapas interactivos (HTML)
├── 📂 scripts/     # Código fuente Python modularizado
   ├── 1_eda_visuals.py    # Visualización Exploratoria
   ├── 2_sql_analysis.py   # Consultas SQL analíticas
   ├── 3_folium_map.py     # Generación de mapas geoespaciales
   ├── 4_dash_app.py       # Aplicación Web / Dashboard
   └── 5_machine_learning.py # Entrenamiento de Modelos
├── 📄 requirements.txt # Dependencias del proyecto
└── 📄 README.md        # Documentación principal
```

## 🛠️ Instalación y Ejecución

Sigue estos pasos para reproducir el análisis en tu entorno local:

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/RubenPA79/SpaceX-Capstone.git
    cd SpaceX-Capstone
    ```

2.  **Crear entorno virtual (Recomendado)**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar módulos**:
    ```bash
    # Ejemplo: Generar el mapa interactivo
    python scripts/3_folium_map.py
    
    # Ejemplo: Lanzar el dashboard
    python scripts/4_dash_app.py
    ```

## 📊 Resultados y Visualizaciones

Los hallazgos clave se encuentran en la carpeta `reports/`. 
- **Mapa de Lanzamientos**: Ver `reports/launch_site_map.html`.
- **Presentación Ejecutiva**: Ver `reports/Final_Presentation_Spacex.pdf`.

---
*Desarrollado por [RubenPA79](https://github.com/RubenPA79)*
