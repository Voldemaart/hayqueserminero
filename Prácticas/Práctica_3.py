import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")
df["longitud_titulo"] = df["Título"].astype(str).apply(len)
df["num_autores"] = df["Autor Personas"].astype(str).apply(lambda x: len(x.split(";")) if x != 'NA' else 0)

# estilo
sns.set(style="whitegrid")

# 1. Gráfico de pastel 
df["Tipo de documento"].value_counts().head(5).plot.pie(autopct='%1.1f%%', figsize=(6, 6), title='Tipos de documento más comunes')
plt.ylabel("")
plt.tight_layout()
plt.show()

# 2. Histograma 
plt.hist(df["longitud_titulo"], bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de la longitud de títulos")
plt.xlabel("Longitud del título")
plt.ylabel("Frecuencia")
plt.show()

# 3. Boxplot
top_lenguas = df["Lengua de publicación"].value_counts().head(5).index
df_filtrado = df[df["Lengua de publicación"].isin(top_lenguas)]
plt.figure(figsize=(10, 6))
sns.boxplot(x="Lengua de publicación", y="longitud_titulo", data=df_filtrado)
plt.title("Longitud de títulos por lengua")
plt.show()

# 4. Scatter plot 
plt.figure(figsize=(8, 6))
sns.scatterplot(x="num_autores", y="longitud_titulo", data=df)
plt.title("Relación entre número de autores y longitud del título")
plt.xlabel("Número de autores")
plt.ylabel("Longitud del título")
plt.show()

# 5. Bar chart 
df["País de publicación"].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Top 10 países con más publicaciones")
plt.xlabel("País")
plt.ylabel("Cantidad de publicaciones")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
