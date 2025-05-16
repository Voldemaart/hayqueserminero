import pandas as pd
from scipy.stats import f_oneway, kruskal
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")
df["longitud_titulo"] = df["Título"].astype(str).apply(len)
df["Lengua de publicación"] = df["Lengua de publicación"].astype(str)

# 3 lenguas más comunes
top_lenguas = df["Lengua de publicación"].value_counts().head(3).index
df_top = df[df["Lengua de publicación"].isin(top_lenguas)]

# distribución
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_top, x="Lengua de publicación", y="longitud_titulo")
plt.title("Longitud de título por lengua")
plt.show()

# Agrupar
grupos = [grupo["longitud_titulo"].values for _, grupo in df_top.groupby("Lengua de publicación")]

# Prueba ANOVA (Análisis de Varianza)
anova_result = f_oneway(*grupos)
print("Resultado ANOVA:")
print(f"F = {anova_result.statistic:.4f}, p = {anova_result.pvalue:.4f}")

# Prueba Kruskal-Wallis (no paramétrica)
kruskal_result = kruskal(*grupos)
print("\nResultado Kruskal-Wallis:")
print(f"H = {kruskal_result.statistic:.4f}, p = {kruskal_result.pvalue:.4f}")
