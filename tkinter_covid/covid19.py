from covid import Covid
from tkinter import *
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
import time
import requests


r = requests.get('https://pomber.github.io/covid19/timeseries.json')
data = r.json()

screen = tk.Tk()
screen.geometry('1000x600')
screen.title('covid-19 tracker')
screen.iconbitmap('mask.ico')
screen.config(bg = '#222436')
screen.resizable(0,0)

def getplt():
    country=country_entry.get()
    country=country.capitalize()
    df = DataFrame(data[country])

    figure = plt.figure()
    subplot = figure.add_subplot(111)
    subplot.plot(df['date'], df['confirmed'], label='confirmed', color='blue')
    subplot.plot(df['date'], df['deaths'], label='deaths', color='red')
    subplot.plot(df['date'], df['recovered'], label='recovered', color='green')
    subplot.legend(loc='upper left')

    start, end = subplot.get_xlim()
    subplot.xaxis.set_ticks(np.arange(start, end, 10))

    for tick in subplot.get_xticklabels():
        tick.set_rotation(45)

    canvas = FigureCanvasTkAgg(figure)
    canvas.get_tk_widget().place(x=400,y=120)
plt.show()



button = Button(screen, command = getplt)
button.place(x = 180 , y = 80 , width = 140 , height   = 30)
button.config(bg = '#FFCB6B' , fg = '#222436' , text = 'plot graph' , font = 'verdana')





def get_stats():
   global country_entry
   ctr=country_entry.get()
   c=Covid()
   stats=c.get_status_by_country_name(str(ctr))
   k="country: "+str(stats['country'])+'\n'+"active cases: "+str(stats['active'])+'\n'+"confirmed cases: "+str(stats['confirmed'])+'\n'+'deaths: '+str(stats['deaths'])+'\n'+'recovered people: '+str(stats['recovered'])
   
   
   display_stats.config(text=str(k))
   


country_entry = Entry(screen)
country_entry.place(x = 10 , y = 20 , height  = 50 , width = 380)
country_entry.config(bg = 'white' , fg = '#222436' , font  = 'verdana')


display_stats = Label(screen)
display_stats.place(x = 10 , y = 120 , width = 380 , height = 260)
display_stats.config(bg = '#A9B8E8' , fg = '#000000' )




get_button = tk.Button(screen , command = get_stats)
get_button.place(x = 80 , y = 80 , width = 90 , height   = 30)
get_button.config(bg = '#FFCB6B' , fg = '#222436' , text = 'Track' , font = 'verdana')





screen.mainloop()


