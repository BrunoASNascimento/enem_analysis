import pandas as pd
import numpy as np


columns_filter = np.array([
    "NU_INSCRICAO",
    "NU_ANO",
    "NU_IDADE",
    "TP_SEXO",
    "TP_COR_RACA",
    "SG_UF_ESC",
    "Q001",
    "Q002",
    "NU_NOTA_COMP1",
    "NU_NOTA_COMP2",
    "NU_NOTA_COMP3",
    "NU_NOTA_COMP4",
    "NU_NOTA_COMP5",
    "NU_NOTA_REDACAO"
])

# encoding='utf-8'
# encoding = "cp1252"
# encoding = "ISO-8859-1"

for i in range(2019, 2020):
    file_name = (f"X:/datasets/enem/microdados/MICRODADOS_ENEM_{i}.csv")
    print(f"Cut data {file_name}.")
    df = pd.read_csv(file_name, sep=";", encoding="ISO-8859-1")
    df = df[columns_filter]
    print(df.shape)
    df.to_csv(
        f'C:/Users/bruno/Developer/github.com/projects/enem_analysis/enem_vs_violencia/data/enem_resume_{i}.csv', index=False)
    df = None
