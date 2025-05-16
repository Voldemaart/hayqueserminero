import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")


df["Fecha de publicación"] = pd.to_datetime(df["Fecha de publicación"], errors='coerce')
df["año_publicacion"] = df["Fecha de publicación"].dt.year


libros_por_anio = df["año_publicacion"].value_counts().sort_index()
libros_por_anio = libros_por_anio[libros_por_anio.index > 1700]  # quitamos años raros o erróneos

#  regresión
X = libros_por_anio.index.values.reshape(-1, 1)  # años
y = libros_por_anio.values  # número de libros

modelo = LinearRegression()
modelo.fit(X, y)

# Predecir desde 1800 hasta 2030
anios_pred = np.arange(1800, 2031).reshape(-1, 1)
predicciones = modelo.predict(anios_pred)

# Mostrar gráfica
plt.figure(figsize=(12, 6))
plt.plot(X, y, label="Datos reales", color="blue")
plt.plot(anios_pred, predicciones, label="Regresión lineal (predicción)", color="red", linestyle="--")
plt.xlabel("Año de publicación")
plt.ylabel("Número de libros")
plt.title("Forecasting: Publicaciones por año")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Imprimir
print("Coeficiente (pendiente):", modelo.coef_[0])
print("Intercepción:", modelo.intercept_)
print("R² Score:", modelo.score(X, y))
