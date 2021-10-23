# -*- coding: utf-8 -*-
from filtros import *
from RF import *

#%% Cargo base y filtro columnas con datos faltantes, NaCl, solvente EtOH y unidades molares
# También quito datos que no se deteminen por TEM, SEM y los datos de referencias

data = carga_datos('Database.csv')

missing = datos_faltantes(data)
grafico_faltantes(missing)
data = drop_columnas_faltantes(data,missing,70) #Quito columnas con menos del 70% de los datos

data = filtro_NaCl(data)
data = filtro_solvente(data)
data = filtro_unidades(data,unit = 'M')

data = filtro_tecnica(data)
data = filtro_referencia(data)
data = filtro_faltantes(data)

#%% Random Forest
#Cuidado que necesita datos todos numéricos y sin faltantes (no sé como hacer que funcione sino) 

X_train, X_test, y_train, y_test = set_train_test(data)

mae,mse,r2 = scores(X_train, X_test, y_train, y_test)
