import pandas as pd

def calcular_retencion_cohorte(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula la tasa de retención por cohorte."""
    resumen = df.groupby('cohorte').agg(
        total_estudiantes=('id_estudiante', 'count'),
        activos=('estatus', lambda x: (x == 'Activo').sum()),
        bajas=('estatus', lambda x: (x == 'Baja').sum())
    ).reset_index()
    
    resumen['tasa_retencion_pct'] = round((resumen['activos'] / resumen['total_estudiantes']) * 100, 2)
    resumen['tasa_desercion_pct'] = round((resumen['bajas'] / resumen['total_estudiantes']) * 100, 2)
    
    return resumen

def calcular_retencion_por_institucion(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula la tasa de retención y deserción por institución educativa."""
    resumen = df.groupby(['institucion', 'tipo_institucion']).agg(
        total_estudiantes=('id_estudiante', 'count'),
        activos=('estatus', lambda x: (x == 'Activo').sum()),
        bajas=('estatus', lambda x: (x == 'Baja').sum())
    ).reset_index()
    
    resumen['tasa_retencion_pct'] = round((resumen['activos'] / resumen['total_estudiantes']) * 100, 2)
    resumen['tasa_desercion_pct'] = round((resumen['bajas'] / resumen['total_estudiantes']) * 100, 2)
    
    return resumen.sort_values(by='tasa_desercion_pct', ascending=False)