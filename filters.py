import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def carga_datos(data_name):
    data = pd.read_csv(data_name,header=0,sep=',',index_col = 0)
    return data

def datos_faltantes(data):
    '''Genera DataFrame de datos faltantes'''
    df = data.copy()
    nan_percent = round(data.isna().mean()*100,1)
    nan_count = data.isna().sum()
    data_percent = 100 - nan_percent
    
    return pd.concat([nan_count.rename('missing_count'), nan_percent.rename('missing_percent'), data_percent.rename('data_percent')],axis=1)

def grafico_faltantes(data_missing):
    '''Grafica el porcentaje de datos de cada columna del DataFrame de missing'''
    data = data_missing.sort_values('data_percent',ascending = False)
    plt.figure(figsize = (15,14), dpi = 200)
    sns.barplot(data = data, y = data.index, x = 'data_percent',color = 'royalblue')
    plt.plot([70,70],[0,19],'--',color='r')
    plt.xlabel('Percentage of existing data (%)',fontsize = 30)
    plt.yticks(fontsize = 30)
    ax = plt.gca()
    for label in ax.get_xticklabels():
        label.set_fontsize(25)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    
    plt.show()

def drop_columnas_faltantes(data,data_missing,porcentaje_completo):
    '''Me saco de encima las columnas con menos del porcentaje_completo de datos indicado'''
    columns_to_drop = [columna for columna in data_missing[data_missing['data_percent'] < porcentaje_completo].index]
    
    return data.drop(labels = columns_to_drop,axis = 1)

def filtro_referencia(data):
    '''Quito columnas de referencia'''
    df = data.copy()
    
    columns_to_drop = ['Year','Reference']
    return df.drop(labels = columns_to_drop,axis = 1)

def filtro_NaCl(data):
    '''Quito datos con agregado de NaCl (un solo paper) 
    y luego la columna de NaCl'''
    df = data.copy()
   
    df = df[df['NaCl concentration'] == 0]
    df = df.drop(['NaCl concentration'],axis = 1)
    
    return df

def filtro_tiempo(data,t_min = 180):
    '''Quito datos con tiempos menores a t_min 
    y luego la columna de tiempo. Me quedo con datos no cinéticos'''
    df = data.copy()
    
    filt1 = df['Time'] > t_min
    filt2 = df['Time'].isna()
    df = df[filt1 | filt2]
    
    df = df.drop(['Time'],axis = 1)
    
    return df

def filtro_solvente(data,solvente = 'EtOH'):
    '''Me quedo solo con filas con el solvente indicado, 
    puede ser EtOH, BuOH, PrOH, MeOH, MeOH-EtOH, IMS, IPA. Luego quita la columna de alcohol.'''
    df = data.copy()
    
    df = df[df['Alcohol'] == solvente]
    df = df.drop(['Alcohol'],axis = 1)
    
    return df

def filtro_unidades(data,unit = 'M'):
    '''Me quedo solo con filas con la unidad de concentración indicada, 
    puede ser M, mol, %m/m, mL. Luego quita la columna de alcohol.'''
    df = data.copy()
    
    df = df[df['Concentration Units'] == unit]
    df = df.drop(['Concentration Units'],axis = 1)
    
    return df

def filtro_concentraciones_size(data,TEOS = 0.6,NH3 = 3, H2O = 20,size = (250,300)):
    '''Quito datos con concentraciones menores a las indicadas (para teos, nh3 y agua).
    También quito valores de tamaño entre los valores indicados en la cupla "size"
    '''
    df = data.copy()
    
    df = df[df['TEOS concentration'] < TEOS]
    df = df[df['Ammonia concentration'] < NH3]
    df = df[df['Water concentration'] < H2O]
    
    filt1 = df['Size'] > size[0]
    filt2 = df['Size'] < size[1]
    df = df[filt1 & filt2]
    
    return df

def filtro_tecnica(data):
    '''Me quedo solo con datos medidos con TEM y SEM'''
    df = data.copy()
    
    filt1 = df['Measurement technique'] == 'TEM'
    filt2 = df['Measurement technique'] == 'SEM'
    df = df[filt1 | filt2]
    
    df = df.drop(['Measurement technique'],axis = 1)
    
    return df

def filtro_faltantes(data):
    '''Elimino filas que tengan datos faltantes'''
    df = data.copy()
    
    df = df.dropna()
    
    return df
