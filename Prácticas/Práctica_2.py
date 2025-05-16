import pandas as pd

ruta_limpio = "C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv"
df = pd.read_csv(ruta_limpio)


print(df.info())
print(df.head())

# fecha a datetime
df["Fecha de publicación"] = pd.to_datetime(df["Fecha de publicación"], errors='coerce')

# longitud del título
df["longitud_titulo"] = df["Título"].astype(str).apply(len)

# número de autores personas
df["num_autores"] = df["Autor Personas"].apply(lambda x: len(str(x).split(";")))

#  Estadísticas generales
print("\nEstadísticas generales:")
print(df[["longitud_titulo", "num_autores"]].describe())

# Agrupar por país y obtener estadísticas
agrupado_pais = df.groupby("País de publicación")[["longitud_titulo", "num_autores"]].mean()
print("\nEstadísticas agrupadas por país:")
print(agrupado_pais.head())

# Agrupar por lengua
agrupado_lengua = df.groupby("Lengua de publicación")[["longitud_titulo", "num_autores"]].mean()
print("\nEstadísticas agrupadas por lengua:")
print(agrupado_lengua.head())

# Distribución de documentos por tipo
print("\nDocumentos por tipo:")
print(df["Tipo de documento"].value_counts())
