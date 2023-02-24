import PySimpleGUI as gui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from modules import (draw_plot)

_VARS = {'window' : False}
plot_generated = False



"""

for BrightColors':
mainCol = #b4fab4
secondCol = #ffa0dc
accentCol = #5d384f

for lightbrown7:
mainCol = '#f6c89f'
secondCol = '#396362'
accentCol = '#f7f9f9'

"""

def draw_figure(figure, canvas):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def create_gui():
    AppFont = 'Any 16'
    gui.theme('LightBrown7')
    mainCol = '#f6c89f'
    secondCol = '#396362'
    accentCol = '#f7f9f9'
    
    exitCol = [[gui.Button('EXIT', font=AppFont)]]

    layout = [[gui.Button("PICK A FOLDER", font=AppFont)],
            [gui.Text("DIRECTORY PATH : ", key="DIR PATH",
                    justification='c', font=AppFont)],
            [gui.Button("SHOW PLOT", font=AppFont)],
            [gui.Button("PICK DESTINATION", font=AppFont)],
            [gui.Text("DESTINATION PATH : ",  key='DEST PATH', font=AppFont)],
            [gui.Button("FILTER FILES", font=AppFont)],
            [gui.Text("", key="progress", font=AppFont)],
            [gui.Canvas(key='figCanvas')],
            [gui.Column(exitCol, element_justification='right', expand_x=True)]
            ]

    _VARS['window'] = gui.Window('Relative Sharpness Tool',
                                layout,
                                finalize=True,
                                resizable=True)

def run_gui():

    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == gui.WIN_CLOSED or event == 'EXIT':
            return {0: 'closed with exit'}
        if event == 'PICK A FOLDER'
