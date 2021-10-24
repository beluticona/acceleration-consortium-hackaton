from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Hackathon - TEAM DQI-FCEN-UBA")
root.geometry("500x700")

#preddict
def preddict():
    
    y_predicted = modelo.predict(X_test)
    #modelo.predict([[TEOS_concentration_entry.get(), ammonia_concentration_entry.get(), water_concentration_entry.get(), temperature_entry.get(), time_entry.get()]]) 

   

    preddiction_label["text"] = "The preddiction is:  " + str(modelo.predict([[TEOS_concentration_entry.get(), ammonia_concentration_entry.get(), water_concentration_entry.get(), temperature_entry.get(), time_entry.get()]]) ) + "  nm"

    #Clear the text boxes
    TEOS_concentration_entry.delete(0,END)
    ammonia_concentration_entry.delete(0,END)
    water_concentration_entry.delete(0,END)
    temperature_entry.delete(0,END)
    time_entry.delete(0,END)


    return

#Entries
TEOS_concentration_entry = Entry(root, width=10)
TEOS_concentration_entry.grid( row=0, column=1, padx=30)
ammonia_concentration_entry = Entry(root, width=10)
ammonia_concentration_entry.grid( row=2, column=1, padx=30)
water_concentration_entry = Entry(root, width=10)
water_concentration_entry.grid( row=3, column=1, padx=30)
temperature_entry = Entry(root, width=10)
temperature_entry.grid( row=4, column=1, padx=30)
time_entry = Entry(root, width=10)
time_entry.grid( row=5, column=1, padx=30)
# size_entry = Entry(root, width=10)
# size_entry.grid( row=6, column=1, padx=30)
# reference_entry = Entry(root, width=10)
# reference_entry.grid( row=8, column=1, padx=30)

#Labels
TEOS_concentration_label = Label(root, text="TEOS concentration")
TEOS_concentration_label.grid( row=0, column=0)
ammonia_concentration_label = Label(root, text="Ammonia concentration")
ammonia_concentration_label.grid( row=2, column=0)
water_concentration_label = Label(root, text="Water concentration")
water_concentration_label.grid( row=3, column=0)
temperature_label = Label(root, text="Temperature")
temperature_label.grid( row=4, column=0)
time_label = Label(root, text="Time")
time_label.grid( row=5, column=0)
# size_label = Label(root, text="Size")
# size_label.grid( row=6, column=0)
# reference_label = Label(root, text="Reference")
# reference_label.grid( row=8, column=0)

""" submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid( row=9, column=0, columnspan=3) """
preddict_btn = Button(root, text="Preddict the Size", command=preddict)
preddict_btn.grid( row=10, column=0, columnspan=3)

preddiction_label = Label(root, text="The preddiction is:")
preddiction_label.grid( row=11, column=0, columnspan=3)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


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
    
    return mae,mse,r2, modelo, y_predicted


raw_data = pd.read_csv("/home/dao/Descargas/Database v2.csv")
raw_data=raw_data.drop(labels = ['Reference'],axis = 1)

X_train, X_test, y_train, y_test = set_train_test(raw_data,test_size = 0.33,semilla = 0)
mae,mse,r2, modelo, y_predicted = scores(X_train, X_test, y_train, y_test)


figure1 = plt.Figure(figsize=(5,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().grid( row=12, column=0, columnspan=4)
ax1.scatter(y_test.values.tolist(),y_predicted,)
ax1.set_title('y_predicted Vs. y_test')
ax1.set_ylabel("y_predicted (nm)", fontsize=14)
ax1.set_xlabel("y_test (nm)", fontsize=14)

#print( modelo.predict([[0.2, 1, 10, 20, 180]]) ) 
#[506.0961]

root.mainloop()