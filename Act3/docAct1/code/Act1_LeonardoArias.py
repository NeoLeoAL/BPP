'''
Autor: Leonardo
Versión: 1.0
Descripción: Programa que lee un csv, trata los datos del mismo, realiza algunas operaciones con ellos,
y finalmente muestra una grafica.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class countColumError(Exception):
    pass      


def createList(df):
    '''Función que crea las listas con los totales de gastos e ingresos mensuales para los datos de la gráfica.'''
    gastos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ingresos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    index = 0
    
    for value in df.values:
        for v in value:
            if v > 0:
                ingresos[index] += v
            else:
                gastos[index] += v
                
            index += 1
        index = 0

    return gastos, ingresos

def createGrafica(df):
    '''Función para crear una gráfica con el total de gastos e ingresos cada mes.'''

    labels = df.columns
    gastos, ingresos = createList(df)

    x = np.arange(len(labels))  # the label locations

    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, gastos, width, label='Gastos')
    rects2 = ax.bar(x + width/2, ingresos, width, label='Ingresos')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Valores')
    ax.set_title('Ingresos y Gastos Mensuales')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def calculoTotales(df):       
    '''Función que realiza y muestra los calculos sobre el dataframe'''
       
    dx = df.sum(skipna=True, numeric_only=True)
        
    print(dx)
    print("\nMayor gasto: " + str(dx.min()))
    print("Menor gasto: " + str(dx.max()))
    print("Media gasto al año: " + str(dx.mean()))
    print("Gasto total al año: " + str(df[df < 0].sum().sum()))
    print("Ingresos totales al año: " + str(df[df > 0].sum().sum()))

def checkColumnType(df):
    '''
    Función que comprueba el tipo de columna.
    En caso de ser tipo object la convierte en numerica.
    '''
    for colum in df.columns[:]:
        if df[colum].dtype == object:
            df[colum] = pd.to_numeric(df[colum], errors='coerce') # Cambia los valores str no numericos por NaN
            
    return df.fillna(0) # Reemplaza los valos NaN por 0

def countColumn(columns):
    '''Función que comprueba si el dataframe tiene 12 columnas.'''
    
    try:
        if len(columns) != 12:
            raise countColumError
        else:
            return 'OK'
    except countColumError:
        print("El contenido del archivo no es correcto.")

def readCsv(csv):
    '''Función que lee el csv y lo devuelve para convertirlo en dataframe.'''
    
    try:
        return pd.read_csv(csv, sep="\s+")
    except IOError:
        print("El archivo no se ha encontrado o no es posible leerlo.")
    except pd.errors.EmptyDataError:
        print("El archivo está vacío.")

def __init__():
    '''Función de inicio con la llamada a las diferentes funciones del programa.'''
    df = readCsv('finanzas2020.csv')
    
    countColumn(df.columns)
    df = checkColumnType(df)     
    calculoTotales(df)
    createGrafica(df)
   
#__init__()