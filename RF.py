from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from filtros import *

def set_train_test(data,test_size = 0.33,semilla = 0):
    '''Separamos en set de entrenamiento y validacion. 
    Necesito dataset sin columnas de referencias, unidad y solvente''' 
    df = data.copy()
    
    y = df['Size']
    x = df.drop(labels = ['Size'],axis = 1)

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size = test_size, random_state = semilla) #implantamos semilla

    return X_train, X_test, y_train, y_test

def forest(X_train,y_train):
    '''Modelamos usando Random forest'''
    
    forest = RandomForestRegressor()
    
    forest.fit(X_train, y_train)
    return forest

def scores(X_train, X_test, y_train, y_test):
    
    modelo = forest(X_train,y_train)
    
    y_predicted = modelo.predict(X_test)
        
    mae = metrics.mean_absolute_error(y_test, y_predicted) #calcula mean absolute error
    mse = metrics.mean_squared_error(y_test, y_predicted) #calcula mean squared error
    r2 = metrics.r2_score(y_test, y_predicted) #calcula R cuadrado
    
    return mae,mse,r2
