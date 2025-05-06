import pandas as pd
import matplotlib.pyplot as plt


df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

# Asumiendo que las columnas con valoraciones se llaman 'tomatometer_rating' y 'audience_rating'
# Ajusta los nombres si son diferentes
critic_col = 'tomatometer_rating'
audience_col = 'audience_rating'

# 11. Calcular promedio de valoración por críticos y audiencia
if critic_col in df_movies.columns and audience_col in df_movies.columns:
    promedio_criticos = df_movies[critic_col].mean()
    promedio_audiencia = df_movies[audience_col].mean()

    print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
    print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

    # 12. Calcular la diferencia entre audiencia y críticos para cada película
    df_movies['diferencia_valoracion'] = df_movies[audience_col] - df_movies[critic_col]

    # 13. Histograma de las diferencias de valoración
    plt.figure(figsize=(8, 5))
    plt.hist(df_movies['diferencia_valoracion'].dropna(), bins=20, edgecolor='black')
    plt.title('Histograma de las diferencias de valoración (Audiencia - Críticos)')
    plt.xlabel('Diferencia de valoración')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
else:
    print(f"Columnas '{critic_col}' o '{audience_col}' no encontradas en el DataFrame.")


