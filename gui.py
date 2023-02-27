import PySimpleGUI as gui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# from hover.hover import *

from modules import (open_image, format_axes)

sc = False


"""

for BrightColors':
mainCol = #b4fab4
secondCol = #ffa0dc
accentCol = #5d384f

for lightbrown7:
mainCol = '#f6c89f'
secondCol = '#396362'
accentCol = '#f7f9f9'

for Topanga:
mainCol = '#282923'
secondCol = '#284b5b'
accentCol = '#dacf6f'

# LightBrown7 = {"main" : '#f6c89f', 
#                "sec" : '#396362',
#                "acc" : '#f7f9f9'}
# Topanga = {"main" : '#282923', 
#                "sec" : '#284b5b',
#                "acc" : '#dacf6f'}
# BrightColors = {"main": '#b4fab4',
#                 "sec": '#ffa0dc',
#                 "acc": '#5d384f'}
"""

def draw_figure(figure, canvas):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg



def create_gui(theme):
    _VARS = {'window' : False}
    plot_generated = False

    AppFont = 'Any 16'
    gui.theme(theme)

    exitCol = [[gui.Button('EXIT', font=AppFont)]]

    layout = [[gui.Button("PICK A FOLDER", font=AppFont)],
            [gui.Text("DIRECTORY PATH : ", key="DIR PATH",
                    justification='c', font=AppFont)],
            [gui.Button("SHOW PLOT", font=AppFont)],
            [gui.Canvas(key='figCanvas')],
            [gui.Column(exitCol, element_justification='right', expand_x=True)]
            ]
    _VARS['window'] = gui.Window('Relative Sharpness Tool',
                                layout,
                                finalize=True,
                                resizable=True)
    return _VARS

def generate_plot_fig(pictures, mean, std, window, face_col='#fff'):
    data = format_axes(pictures)
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')


    sc = plt.scatter(x=data['x'], y=data['y'], c=data['col'])

    def onClick(event):
        cont, ind = sc.contains(event)
        if cont:
            idx = ind["ind"][0]
            # print(data['x'])
            # print(data['y'])
            print(pictures[idx])
            open_image(pictures, idx)
            

    plt.axhline(y=mean, c=face_col['acc'])
    plt.axhline(y=mean - std, c='white', linestyle="dashed")
    plt.axhline(y=mean + std, c='white', linestyle="dashed")
    plt.xlabel("Picture Number", fontweight='bold', c=face_col['acc'])
    plt.ylabel("Relative Sharpness", fontweight='bold', c=face_col['acc'])
    plt.grid()
    fig.set_facecolor(face_col['main'])
    fig.canvas.mpl_connect("button_press_event", onClick)
    draw_figure(fig, window['window']['figCanvas'].TKCanvas)

    
