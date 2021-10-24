from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Hackathon - TEAM DQI-FCEN-UBA")
root.geometry("300x200")

#submit
def submit():
    

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
size_entry = Entry(root, width=10)
size_entry.grid( row=6, column=1, padx=30)
reference_entry = Entry(root, width=10)
reference_entry.grid( row=8, column=1, padx=30)

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
size_label = Label(root, text="Size")
size_label.grid( row=6, column=0)
reference_label = Label(root, text="Reference")
reference_label.grid( row=8, column=0)

submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid( row=9, column=0, columnspan=3) 




root.mainloop()
