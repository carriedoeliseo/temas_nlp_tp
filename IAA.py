import sys, krippendorff
import pandas as pd
import numpy as np

def matriz_kripp (dataset):
    # copio dataset
    data = dataset.copy()

    # anotadores
    anotadores = data["Nombre anotador(a)"].unique()

    # agrego anotaciones
    anotaciones = {}
    for ann in anotadores:
        anotaciones_ann = data[data["Nombre anotador(a)"] == ann].copy()
        anotaciones_ann = anotaciones_ann.sort_values(by="nro")
        anotaciones_ann = anotaciones_ann.iloc[:,-1].values
        anotaciones_ann = pd.Series(map(lambda a : a.strip(), anotaciones_ann))

        anotaciones[ann] = anotaciones_ann

    # convierto en DataFrame, printeamos y devolvemos matriz
    df = pd.DataFrame(anotaciones)
    print("\n", df)
    return df.values.T.astype(str)

def main ():
    # leo dataset anotado
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]
    dataset = pd.read_excel(file_name, sheet_name=sheet_name)

    # genero matriz
    matriz = matriz_kripp(dataset)

    # calculo IAA
    domain = ["Antisemita", "Negativo", "Indefinido"]
    alpha = krippendorff.alpha(reliability_data=matriz, level_of_measurement='nominal', value_domain=domain)
    print('\nIAA: ', alpha)


if __name__ == '__main__':
    main()