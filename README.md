# Análisis y Predicción de Aterrizajes del Falcon 9 de SpaceX

Este repositorio contiene el proyecto final (Capstone) para la certificación de Ciencia de Datos. El objetivo es predecir si la primera etapa del cohete Falcon 9 aterrizará con éxito, lo cual es crucial para determinar el costo de los lanzamientos.

## Estructura del Proyecto

El proyecto se ha automatizado mediante scripts de Python para garantizar la reproducibilidad de los resultados.

### 1. Scripts de Análisis (`/scripts`)
*   `data_manager.py`: Descarga y gestiona los datasets originales de la API de SpaceX y fuentes proporcionadas.
*   `1_eda_visuals.py`: Genera visualizaciones para el Análisis Exploratorio de Datos (EDA).
*   `2_sql_analysis.py`: Crea una base de datos SQLite y ejecuta consultas SQL para obtener insights clave.
*   `3_folium_map.py`: Genera un mapa interactivo (`launch_site_map.html`) visualizando los sitios de lanzamiento y sus tasas de éxito.
*   `4_dash_app.py`: Código fuente para el dashboard interactivo utilizando Plotly Dash.
*   `5_machine_learning.py`: Entrena y evalúa modelos predictivos (Regresión Logística, SVM, Árboles de Decisión, KNN).
*   `generate_pptx.py`: Script de automatización que generó la presentación final.

### 2. Resultados (`/assets`)
*   **EDA**: Gráficos de tendencias temporales, carga útil vs. éxito, y éxito por órbita.
*   **SQL**: Reporte de texto con los resultados de las consultas a la base de datos (`sql/results.txt`).
*   **Machine Learning**: Matrices de confusión y gráficos comparativos de precisión de los modelos (`ml/`).

### 3. Mapa Interactivo
*   `launch_site_map.html`: Mapa HTML interactivo generado con Folium.

## Ejecución

Para reproducir el análisis, ejecute los scripts en orden numérico:

```bash
python scripts/1_eda_visuals.py
python scripts/2_sql_analysis.py
python scripts/3_folium_map.py
# ... etc
```

## Autor
Proyecto Capstone de Ciencia de Datos.
