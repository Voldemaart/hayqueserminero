import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv")

# temas
texto = " ".join(df["Tema"].dropna().astype(str).tolist())

# nubeee
wordcloud = WordCloud(width=1000, height=600,
                      background_color='white',
                      colormap='viridis',
                      max_words=200,
                      contour_color='steelblue').generate(texto)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Nube de Palabras - Temas de libros")
plt.tight_layout()
plt.show()
