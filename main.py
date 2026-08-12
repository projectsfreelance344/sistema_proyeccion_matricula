import os
import pandas as pd
from src.data_loader.scraper_coacalco import obtener_escuelas_coacalco_denue, generar_dataset_estudiantes_reales
from src.analytics.metrics import calcular_retencion_cohorte, calcular_retencion_por_institucion
from src.analytics.model import cargar_y_combinar_datos, entrenar_evaluar_riesgo
from src.database.db_manager import guardar_en_sqlite
from src.analytics.charts import generar_grafico_retencion, generar_matriz_riesgo

def main():
    print("=== PLATAFORMA INTEGRAL DE DESERCIÓN (COACALCO DATA PIPELINE) ===")

    # 1. Rutas
    output_raw = os.path.join("data", "raw", "estudiantes.csv")
    input_contexto = os.path.join("data", "external", "coacalco_contexto.csv")
    output_dir = os.path.join("data", "processed")
    os.makedirs(output_dir, exist_ok=True)

    # 2. Extracción / Scraping
    print("\n[1/6] Extrayendo oferta educativa real de Coacalco de Berriozábal...")
    df_escuelas = obtener_escuelas_coacalco_denue()
    df_estudiantes = generar_dataset_estudiantes_reales(df_escuelas, num_registros=20)
    df_estudiantes.to_csv(output_raw, index=False)
    print(f"-> Generada muestra anonimizada de {len(df_estudiantes)} alumnos en planteles de Coacalco.")

    # 3. Carga y Combinación
    print("\n[2/6] Cruzando datos académicos con contexto socioeconómico...")
    df_completo = cargar_y_combinar_datos(output_raw, input_contexto)

    # 4. Métricas por Institución Real
    print("\n[3/6] Tasa de retención por INSTITUCIÓN EN COACALCO:")
    df_institucion = calcular_retencion_por_institucion(df_completo)
    print(df_institucion.to_string(index=False))

    # 5. Modelo ML
    print("\n[4/6] Ejecutando Modelo Predictivo de Riesgo (Random Forest)...")
    df_evaluado = entrenar_evaluar_riesgo(df_completo)

    activos_riesgo = df_evaluado[
        (df_evaluado['estatus'] == 'Activo') &
        (df_evaluado['riesgo_ml'].isin(['MEDIO', 'ALTO']))
    ]

    columnas_mostrar = [
        'id_estudiante', 'institucion', 'promedio', 
        'asistencia_pct', 'probabilidad_desercion_pct', 
        'riesgo_ml', 'motivo_desercion'
    ]

    print("\n-> Alumnos activos en riesgo detectados por ML:")
    if not activos_riesgo.empty:
        print(activos_riesgo[columnas_mostrar].to_string(index=False))
    else:
        print("No se detectaron alumnos activos en nivel de riesgo MEDIO o ALTO en esta muestra.")

    # 6. Persistencia y Visualización
    print("\n[5/6] Guardando base de datos SQLite y reportes...")
    guardar_en_sqlite(df_evaluado, "evaluacion_estudiantes_ml")
    guardar_en_sqlite(df_institucion, "retencion_institucion")
    df_evaluado.to_csv(os.path.join(output_dir, "reporte_integral_coacalco.csv"), index=False)

    print("\n[6/6] Generando gráficos...")
    df_retencion_cohorte = calcular_retencion_cohorte(df_completo)
    generar_grafico_retencion(df_retencion_cohorte)
    generar_matriz_riesgo(df_completo)

    print("\n=== PIPELINE DE DATOS REALES EJECUTADO CON ÉXITO ===")

if __name__ == "__main__":
    main()