import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")

def generar_grafico_retencion(df_retencion: pd.DataFrame, output_dir: str = "data/processed"):
    """Genera un gráfico de barras para la tasa de retención por cohorte."""
    plt.figure(figsize=(8, 5))
    
    ax = sns.barplot(
        data=df_retencion,
        x='cohorte',
        y='tasa_retencion_pct',
        palette='Blues_d',
        hue='cohorte',
        legend=False
    )

    plt.title('Tasa de Retención Estudiantil por Cohorte (%)', fontsize=14, fontweight='bold')
    plt.xlabel('Cohorte de Ingreso', fontsize=11)
    plt.ylabel('Retención (%)', fontsize=11)
    plt.ylim(0, 110)

    for p in ax.patches:
        ax.annotate(f"{p.get_height():.1f}%",
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 7),
                    textcoords='offset points',
                    fontweight='bold')

    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    chart_path = os.path.join(output_dir, 'grafico_retencion_cohorte.png')
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"[GRÁFICO] Guardado: {chart_path}")

def generar_matriz_riesgo(df_estudiantes: pd.DataFrame, output_dir: str = "data/processed"):
    """Genera una matriz de dispersión (Asistencia vs Promedio) clasificada por riesgo."""
    plt.figure(figsize=(9, 6))

    palette_colors = {'BAJO': 'green', 'MEDIO': 'orange', 'ALTO': 'red'}

    sns.scatterplot(
        data=df_estudiantes,
        x='asistencia_pct',
        y='promedio',
        hue='riesgo_ml',
        palette=palette_colors,
        s=100,
        alpha=0.8
    )

    plt.axhline(7.0, color='red', linestyle='--', alpha=0.5, label='Umbral Promedio Crítico')
    plt.axvline(75, color='orange', linestyle='--', alpha=0.5, label='Umbral Asistencia Crítica')

    plt.title('Matriz de Riesgo: Asistencia vs. Promedio Académico', fontsize=14, fontweight='bold')
    plt.xlabel('Porcentaje de Asistencia (%)', fontsize=11)
    plt.ylabel('Promedio General', fontsize=11)
    plt.legend(title='Nivel de Riesgo', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    chart_path = os.path.join(output_dir, 'matriz_riesgo_estudiantes.png')
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"[GRÁFICO] Guardado: {chart_path}")