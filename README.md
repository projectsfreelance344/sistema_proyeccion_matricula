# Sistema de Proyección de Matrícula y Retención Estudiantil (Coacalco Data Pipeline)

Plataforma de analítica predictiva y arquitectura de datos End-to-End desarrollada en Python para el diagnóstico de la retención académica, la proyección de matrícula y la identificación oportuna de estudiantes activos en riesgo de deserción en instituciones de educación superior de Coacalco de Berriozábal.

---

## 📌 Descripción General

El proyecto simula y procesa datos académicos y socioeconómicos del municipio de Coacalco para ofrecer una herramienta operativa a tomadores de decisión educativos. A través de un pipeline automatizado, el sistema combina datos de oferta universitaria local, evalúa patrones de rendimiento y asistencia, entrena un modelo de Machine Learning para predecir niveles de riesgo (Bajo, Medio, Alto) e identifica la **causa raíz del riesgo de deserción** (problemas económicos, transporte/distancia, incompatibilidad laboral, entre otros).

---

## 🛠️ Arquitectura del Proyecto

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