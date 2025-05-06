import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

df_movies_copy = df_movies.copy()

df_genres_exploded = df_movies_copy.assign(
genre=df_movies_copy['genre'].str.split(',')
).explode('genre')

df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

genre_ratings = df_genres_exploded.groupby('genre')['audience_rating'].mean()

top_10_genres = genre_ratings.sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 8))
top_10_genres.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Top 10 peliculas con mejor promedio')
plt.ylabel('')
plt.show()



