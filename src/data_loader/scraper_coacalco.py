import random
import pandas as pd

def obtener_escuelas_coacalco_denue() -> pd.DataFrame:
    """Devuelve la oferta educativa simulada de instituciones en Coacalco."""
    escuelas = [
        {"nombre": "TESCo (Tecnológico de Estudios Superiores de Coacalco)", "tipo": "publica"},
        {"nombre": "FES Iztacala UNAM (Zona de Influencia Coacalco)", "tipo": "publica"},
        {"nombre": "UVM Campus Hispano", "tipo": "privada"},
        {"nombre": "Universidad Lucerna Coacalco", "tipo": "privada"}
    ]
    return pd.DataFrame(escuelas)

def generar_dataset_estudiantes_reales(df_escuelas: pd.DataFrame, num_registros: int = 20) -> pd.DataFrame:
    """Genera estudiantes anonimizados con motivos de deserción."""
    motivos_posibles = [
        "Problemas Económicos",
        "Distancia y Transporte (Coacalco/CDMX)",
        "Incompatibilidad Horario Laboral",
        "Bajo Rendimiento Académico",
        "Motivos Personales / Salud"
    ]
    
    registros = []
    for i in range(1, num_registros + 1):
        escuela = df_escuelas.sample(1).iloc[0]
        estatus = random.choices(["Activo", "Baja", "En Riesgo"], weights=[0.7, 0.2, 0.1])[0]
        
        # Asignamos motivo si está dado de Baja O en nivel de Riesgo
        if estatus in ["Baja", "En Riesgo"]:
            motivo = random.choice(motivos_posibles)
        else:
            motivo = "N/A (Activo Sin Riesgo)"
        
        registros.append({
            "id_estudiante": f"EST{i:03d}",
            "genero": random.choice(["M", "F"]),
            "edad": random.randint(18, 25),
            "institucion": escuela["nombre"],
            "tipo_institucion": escuela["tipo"],
            "codigo_postal": random.choice([55700, 55710, 55712, 55714, 55717]),
            "promedio": round(random.uniform(6.0, 9.8), 1),
            "asistencia_pct": round(random.uniform(60.0, 100.0), 1),
            "cohorte": random.choice(["2023-1", "2023-2", "2024-1"]),
            "estatus": estatus,
            "motivo_desercion": motivo
        })
        
    return pd.DataFrame(registros)