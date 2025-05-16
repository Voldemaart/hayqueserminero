import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.compose import ColumnTransformer

df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")

df["longitud_titulo"] = df["Título"].astype(str).apply(len)
df["num_autores"] = df["Autor Personas"].astype(str).apply(lambda x: len(x.split(";")) if pd.notnull(x) else 0)
df["Fecha de publicación"] = pd.to_datetime(df["Fecha de publicación"], errors='coerce')
df["año_publicacion"] = df["Fecha de publicación"].dt.year.fillna(0).astype(int)


df = df[df["Género/Forma"].notnull()]
df = df[df["Género/Forma"] != 'NA']  # Si usaste 'NA' para rellenar


y = df["Género/Forma"]
X = df[["longitud_titulo", "num_autores", "año_publicacion"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))

