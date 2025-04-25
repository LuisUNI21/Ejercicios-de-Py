
import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 8. ¿Cuántas películas hay en total? Mostrar en consola

total_peliculas = len(df_movies)
print(f"Total de películas: {total_peliculas}")

# 10.¿Cuántas películas fueron calificadas como "Certified Fresh", "Fresh" y "Rotten"? usa value counts sobre la columna tomatometer_status

conteo_tomatometer = df_movies['tomatometer_status'].value_counts()

print("\nConteo por clasificación del tomatometer:")
print(conteo_tomatometer)

# Gráfico de pastel (pie chart)

plt.figure(figsize=(6, 6))
conteo_tomatometer.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff6347', '#90ee90', '#ffd700'])
plt.title('Distribución de Clasificaciones Tomatometer')
plt.ylabel('')  # Oculta la etiqueta del eje Y
plt.tight_layout()
plt.show()
