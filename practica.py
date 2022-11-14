
#muestra un gráfico
#de uso de m3 y de número de clientes

import pandas as pd
import matplotlib.pyplot as plt

def practica():
    datos = pd.read_csv("D:\\adrian\\programacion\\proyectos\\teoria 14-11-2022\\agua.csv")
    df = datos[["Ús","any_","m3_registrats","núm_clients","ObjectId","CODI_ENS","NOM_ENS"]]
    df = datos.rename(columns={
        "Ús": "USOS",
        "any_": "AÑO",
        "m3_registrats": "M3",
        "núm_clients": "NUMERO_DE_CLIENTES",
        "ObjectId": "OBJETIVOS",
        "CODI_ENS": "CODIGO",
        "NOM_ENS": "NOMBRE_EMPRESA"
    })

    m3_por_uso = df.groupby("USOS")["M3"].mean()
    m3_por_uso.head(10).plot.barh()
    plt.show()

    df.M3.plot.hist()
    plt.show()





practica()