import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

directores_frecuentes = df_movies['directors'].value_counts()

top_10_directores = directores_frecuentes.head(10).index

df_top_directores = df_movies[df_movies['directors'].isin(top_10_directores)]

promedios_rating = df_top_directores.groupby('directors')['tomatometer_rating'].mean()

top_5_rating = promedios_rating.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_5_rating.plot(kind='bar', color='blue')
plt.title('Calificacion promedio de los 10 directores mas frecuentes')
plt.ylabel('Director')
plt.xticks(rotation=45)
plt.show()