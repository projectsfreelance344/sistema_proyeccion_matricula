# 📊 Sistema de Proyección de Matrícula y Deserción Estudiantil (Coacalco Data Pipeline)

Plataforma de analítica predictiva y arquitectura de datos End-to-End desarrollada en Python para el diagnóstico de la deserción académica, la proyección de matrícula y la identificación oportuna de estudiantes activos en riesgo de deserción en instituciones de educación superior de Coacalco de Berriozábal.

---

## 🎯 Caso de Uso

Automatización del diagnóstico de permanencia académica y proyección de matrícula en la región de Coacalco. Sustituye el análisis manual en hojas de cálculo por un pipeline de datos dinámico que cruza contexto socioeconómico local con algoritmos de Machine Learning para detectar patrones de deserción y emitir alertas preventivas.

---

## 🏗️ Arquitectura del Proyecto

```text
sistema_proyeccion_matricula/
├── data/
│   ├── external/
│   │   └── coacalco_contexto.csv       # Contexto socioeconómico por zona/CP
│   ├── processed/                      # Reportes CSV y gráficos generados
│   │   ├── grafico_retencion_cohorte.png
│   │   ├── matriz_riesgo_estudiantes.png
│   │   └── reporte_integral_coacalco.csv
│   └── raw/
│       └── estudiantes.csv             # Extracción primaria anonimizada
├── database/
│   └── matricula_coacalco.db           # Base de datos SQLite persistente
├── src/
│   ├── analytics/
│   │   ├── charts.py                   # Visualización automatizada (Seaborn/Matplotlib)
│   │   ├── metrics.py                  # Agregaciones de retención por cohorte/plantel
│   │   └── model.py                    # Pipeline de ML con Random Forest
│   ├── data_loader/
│   │   └── scraper_coacalco.py         # ETL y simulación de oferta educativa real
│   └── database/
│       └── db_manager.py               # Módulo de persistencia SQLite
├── .gitignore                          # Exclusión de entornos virtuales y temporales
├── main.py                             # Orquestador principal del pipeline
└── requirements.txt                    # Dependencias del proyecto