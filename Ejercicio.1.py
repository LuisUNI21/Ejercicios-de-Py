
# 1. Importar las librerías necesarias

import pandas as pd

# 2. Leer el archivo CSV

df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

# 3. Mostrar las primeras filas del DataFrame para revisar su contenido

print("Primeras filas del DataFrame:")
print(df_movies.head())

# 4. Verificar los nombres de las columnas

print("\nNombres de las columnas:")
print(df_movies.columns)

# 5. Convertir la columna 'in_theaters_date' al tipo datetime

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 6. Verificar que la conversión fue exitosa (dtypes)

print("\nTipos de datos después de la conversión:")
print(df_movies.dtypes)

# 7. Mostrar si hubo valores no convertidos (NaT)

missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")
