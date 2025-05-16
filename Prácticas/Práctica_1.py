import pandas as pd
import glob
import os

def leer_y_concatenar_archivos(ruta_archivos):
    archivos = glob.glob(ruta_archivos)
    dataframes = [pd.read_csv(archivo, sep=";", engine="python") for archivo in archivos]
    df_final = pd.concat(dataframes, ignore_index=True)
    return df_final

def eliminar_columnas(df, columnas_a_eliminar):
    columnas_a_eliminar = [col for col in columnas_a_eliminar if col in df.columns]
    df = df.drop(columns=columnas_a_eliminar)
    return df

def eliminar_nulo_columna(df, nulos_en_columnas):
    df = df.dropna(subset=nulos_en_columnas)  
    return df


def main():
    ruta_archivos = r"C:\Users\mar_v\OneDrive\Documentos\2025\Minería\Datos csv\*.csv"
    
    # unir archivos
    df_final = leer_y_concatenar_archivos(ruta_archivos)
    print("Archivos combinados correctamente.")
    print("Forma inicial del DataFrame:", df_final.shape)

    # columnas a eliminar
    columnas_a_eliminar = [
        'Descripción y notas', 'Citas o referencias', 'transcripciones de interés', 'Procedencia', 'Intérpretes', 'Resumen',
        'Premios', 'Periodicidad', 'Lugar relacionado', 'Forma de la composición sonora', 'Forma de la composición notada',
        'tipo material cartográfico', 'Proyección del mapa', 'Escala del mapa', 'CDU', 'Otra clasificación', 'id registros relacionados',
        'información asociada a registros relacionados', 'id otras ediciones', 'información asociada a otras ediciones',
        'id título anterior', 'información asociada a título anterior', 'id título posterior', 'información asociada a título posterior',
        'ISBN', 'ISSN', 'Depósito Legal', 'Otros Números Normalizados', 'Número Bibliografía Nacional','texto_OCR','Condiciones de uso',
        'otras lenguas','Lengua original','Editor musical','Información asociada al título','Título uniforme','Otros Títulos','Contenido',
        'version_digital'
    ]

    nulos_en_columnas = [
        'Autor Personas','Lugar de publicación','Fecha de publicación','Descripción física','Editorial','País de publicación',
        'Lengua de publicación','Serie','Tema','signatura'
        ]

    # Eliminar las columnas
    df_final = eliminar_columnas(df_final, columnas_a_eliminar)
    df_final = eliminar_nulo_columna(df_final, nulos_en_columnas)

   

    print("Forma después de eliminar columnas:", df_final.shape)

    #Ya sólo quedan 3 columnas con valores nulos, como sí los necesito para el ánalisis, rellenaré esos vacíos con 'NA'
    df_final = df_final.fillna('NA')
    
    
    print("Valores nulos por columna:")
    print(df_final.isnull().sum())

    # Guardar el DataFrame limpio
    df_final.to_csv("C:/Users/mar_v/OneDrive/Documentos/2025/Minería/Prácticas/datos_limpios.csv", index=False, encoding="utf-8")
    print("Archivo guardado correctamente como 'datos_limpios.csv'.")

if __name__ == "__main__":
    main()
