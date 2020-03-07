## En la carpeta de "Desarrollo Equitativo">"Inversion cantonal FODESAF" del drive(https://drive.google.com/drive/u/0/folders/1DSpidTVv4_qs8VV_gA8aRRijhoe7sWB1) puede encontrar los conjuntos de datos que se usan en este codigo.

## Yo analice unicamente los de 2014, 2015, 2016. Los de 2012 y 2013 hay que limpiarlos por que tienen filas en blanco. 

## Unicamente use el paquete de pandas: 

import pandas as pd

## definimos una funcion para leer los datos del excel previamente descargado.
def inversion(year):
    df = pd.read_excel('Inversion social publica y beneficiarios por canton {0}.xls'.format(year))
    return df

## unificamos los dataframes:
inversion_fodesaf = pd.concat([pd.concat([inversion(2014),inversion(2015)]),inversion(2016)])
