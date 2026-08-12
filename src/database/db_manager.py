from sqlalchemy import create_engine
import pandas as pd

def guardar_en_sqlite(df: pd.DataFrame, nombre_tabla: str, db_path: str = "sqlite:///data/processed/matricula.db"):
    """Guarda un DataFrame procesado en una base de datos SQLite local."""
    engine = create_engine(db_path)
    df.to_sql(nombre_tabla, con=engine, if_exists='replace', index=False)
    print(f"[BD] Tabla '{nombre_tabla}' guardada exitosamente en la base de datos.")