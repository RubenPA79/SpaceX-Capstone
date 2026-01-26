# Presentación Capstone de Ciencia de Datos - SpaceX

## 1. Resumen Ejecutivo
El objetivo de este proyecto es predecir si la primera etapa del cohete Falcon 9 de SpaceX aterrizará con éxito.
Esto permitiría determinar el costo de un lanzamiento, ya que la reutilización de la primera etapa ahorra costos significativos.
Utilizamos datos de la API de SpaceX y de Wikipedia, realizamos limpieza de datos, análisis exploratorio (EDA), análisis SQL, y construimos modelos de Machine Learning.
**Resultado clave:** El mejor modelo de clasificación alcanzó una precisión de aproximadamente 83% (verificar resultados exactos en `assets/ml/results.txt`).

## 2. Introducción
- **Contexto:** SpaceX busca revolucionar los viajes espaciales reduciendo costos mediante la reutilización de cohetes.
- **Problema:** Determinar si la primera etapa aterrizará exitosamente para estimar el precio del lanzamiento.
- **Enfoque:** Usar datos históricos de lanzamientos para entrenar un modelo de clasificación binaria (1=Éxito, 0=Fallo).

## 3. Metodología
1.  **Recopilación de Datos:** API de SpaceX y Web Scraping de Wikipedia.
2.  **Limpieza de Datos (Data Wrangling):** Manejo de valores nulos, filtrado de Falcon 9.
3.  **Análisis Exploratorio (EDA):** Visualización de relaciones entre variables (Carga útil, Órbita, Sitio de lanzamiento).
4.  **Análisis SQL:** Consultas a base de datos para insights específicos.
5.  **Mapa Interactivo:** Uso de Folium para visualizar sitios de lanzamiento y resultados.
6.  **Dashboard:** Uso de Plotly Dash para exploración interactiva.
7.  **Análisis Predictivo:** Entrenamiento de modelos (Regresión Logística, SVM, Árbol de Decisión, KNN).

## 4. Resultados

### EDA (Visualizaciones)
Se encontraron patrones interesantes:
- **Tendencia Temporal:** La tasa de éxito ha aumentado con los años. `assets/eda/7_yearly_trend.png`
- **Relación Carga-Sitio:** Diferentes sitios manejan diferentes cargas y tasas de éxito. `assets/eda/3_payload_vs_site.png`
- **Órbitas:** Las órbitas ES-L1, GEO, HEO y SSO tienen altas tasas de éxito. `assets/eda/4_success_by_orbit.png`

### SQL
Resultados clave de las consultas (ver `assets/sql/results.txt`):
- Sitios de lanzamiento distintos encontrados.
- Carga total transportada por la NASA.
- Identificación de aterrizajes exitosos y fallidos por fecha.

### Mapa Interactivo (Folium)
El mapa (`launch_site_map.html`) muestra que:
- Los sitios de lanzamiento están cerca de la costa (seguridad).
- Están cerca de vías férreas y carreteras (logística).
- KSC LC-39A tiene una alta tasa de éxito (marcadores verdes).

### Machine Learning (Clasificación)
Se probaron cuatro modelos: Regresión Logística, SVM, Árbol de Decisión y KNN.
- Todos los modelos mostraron un rendimiento similar.
- **Matriz de Confusión:** Muestra la capacidad del modelo para distinguir entre aterrizajes exitosos y fallidos.
- Ver comparación en: `assets/ml/model_comparison.png`

## 5. Conclusiones
- Es posible predecir el éxito del aterrizaje de la primera etapa del Falcon 9 con una precisión considerable.
- La órbita y la masa de la carga útil son factores importantes.
- La tasa de éxito de SpaceX ha mejorado significativamente con el tiempo.
- Los modelos de Machine Learning (SVM, Árboles) son herramientas efectivas para esta predicción.

## Enlaces
- **Repositorio:** [Insertar URL de GitHub aquí]
- **Presentación PDF:** [Insertar nombre del archivo PDF aquí]
