import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")


df["longitud_titulo"] = df["Título"].astype(str).apply(len)
df["num_autores"] = df["Autor Personas"].astype(str).apply(lambda x: len(x.split(";")) if pd.notnull(x) else 0)
df["Fecha de publicación"] = pd.to_datetime(df["Fecha de publicación"], errors='coerce')
df["año_publicacion"] = df["Fecha de publicación"].dt.year.fillna(0).astype(int)

# variables
X = df[["longitud_titulo", "num_autores", "año_publicacion"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-means clustering
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
df["cluster"] = kmeans.fit_predict(X_scaled)

# resumen
print(" Libros por cluster:")
print(df["cluster"].value_counts())
print("\n Estadísticas promedio por cluster:")
print(df.groupby("cluster")[["longitud_titulo", "num_autores", "año_publicacion"]].mean())

# Visualización
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df["año_publicacion"], df["longitud_titulo"],
                      c=df["cluster"], cmap="tab10", alpha=0.6)
plt.xlabel("Año de publicación")
plt.ylabel("Longitud del título")
plt.title("Visualización de Clusters con K-means")
plt.colorbar(scatter, label="Cluster")
plt.grid(True)
plt.tight_layout()
plt.show()
