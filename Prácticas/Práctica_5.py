import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#profe con mis datos no sale una regresión, pero lo intenté

df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")

df["longitud_titulo"] = df["Título"].astype(str).apply(len)
df["num_autores"] = df["Autor Personas"].astype(str).apply(lambda x: len(x.split(";")))

df["Fecha de publicación"] = pd.to_datetime(df["Fecha de publicación"], errors='coerce')
df["año_publicacion"] = df["Fecha de publicación"].dt.year.fillna(0).astype(int)

df["longitud_descripcion"] = df["Descripción física"].astype(str).apply(len)

# Variables para el modelo
variables = ["num_autores", "año_publicacion", "longitud_descripcion"]
X = df[variables]
y = df["longitud_titulo"]

# Matriz de correlación
corr = df[variables + ["longitud_titulo"]].corr()
print("Matriz de correlación:")
print(corr)

# Visualización matriz de correlación
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()

# Modelo de regresión lineal múltiple
modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# R² score
r2 = r2_score(y, y_pred)
print(f"R² Score: {r2:.4f}")

# Coeficientes
coef = pd.DataFrame({
    "Variable": variables,
    "Coeficiente": modelo.coef_
})
print("\nCoeficientes del modelo:")
print(coef)

# Gráfico de residuales (opcional)
plt.figure(figsize=(8,6))
plt.scatter(y_pred, y_pred - y, alpha=0.5)
plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), colors='r', linestyles='dashed')
plt.xlabel("Valores predichos")
plt.ylabel("Residuales")
plt.title("Gráfico de residuales")
plt.show()
