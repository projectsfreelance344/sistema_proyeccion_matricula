import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

def cargar_y_combinar_datos(estudiantes_path: str, contexto_path: str) -> pd.DataFrame:
    """Combina datos académicos de estudiantes con contexto socioeconómico municipal."""
    df_estudiantes = pd.read_csv(estudiantes_path)
    df_contexto = pd.read_csv(contexto_path)
    
    # Merge por Código Postal
    df_merged = pd.merge(df_estudiantes, df_contexto, on='codigo_postal', how='left')
    return df_merged

def entrenar_evaluar_riesgo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Entrena un algoritmo de Random Forest usando variables académicas y externas
    para predecir la probabilidad de deserción.
    """
    df_model = df.copy()
    
    # Mapeo de variables categóricas
    df_model['es_privada'] = (df_model['tipo_institucion'] == 'privada').astype(int)
    
    # Feature Engineering
    features = [
        'promedio', 
        'asistencia_pct', 
        'es_privada', 
        'vulnerabilidad_transporte_pct', 
        'tasa_desempleo_local_pct'
    ]
    
    # Definir Target (1 = Baja/Deserción, 0 = Activo)
    df_model['target_desercion'] = (df_model['estatus'] == 'Baja').astype(int)
    
    X = df_model[features]
    y = df_model['target_desercion']
    
    # Modelo Random Forest
    rf = RandomForestClassifier(n_estimators=50, random_state=42)
    rf.fit(X, y)
    
    # Predecir probabilidad de deserción para todos los alumnos
    df['probabilidad_desercion_pct'] = (rf.predict_proba(X)[:, 1] * 100).round(2)
    
    # Nivel de riesgo basado en probabilidad del modelo
    df['riesgo_ml'] = pd.cut(
        df['probabilidad_desercion_pct'],
        bins=[-1, 30, 60, 100],
        labels=['BAJO', 'MEDIO', 'ALTO']
    )
    
    return df