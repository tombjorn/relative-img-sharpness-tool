from modules import *
from gui import *
import asyncio
import sys
from tkinter.filedialog import askdirectory
import traceback



themes = { "LightBrown7" : 
            {"main" : '#f6c89f', 
            "sec" : '#396362',
            "acc" : '#f7f9f9'},
          "Topanga" : 
            {"main" : '#282923', 
            "sec" : '#284b5b',
            "acc" : '#dacf6f'}, 
          "BrightColors" : 
            {"main": '#b4fab4',
            "sec": '#ffa0dc',
            "acc": '#5d384f'}}


def main():
    global pictures
    plot_generated = False
    # threshold = float(sys.argv[1])
    theme = 'LightBrown7'
    gui = create_gui(theme)

    # print(f'_VARS RETURNED FROM CREATE_GUI() :{gui}')
    pictures = []

    while True:
        # print(f'_VARS INSIDE WHILE LOOP: {gui}')
        event, values = gui['window'].read(timeout=200)


        if event == 'EXIT':
            # print('exit event')
            break

        if event == "PICK A FOLDER":
            path = askdirectory(title='Image directory')
            gui['window']['DIR PATH'].update(f'DIRECTORY PATH : {path}')

        if event == "SHOW PLOT":
            threshold = float(values[0])
            try:

                pictures = generate_pictures(path)
                sharp_m = mean(pictures)
                sharp_s = std(pictures)

                for p in pictures:
                    img = p['instance']
                    img.get_col(t=threshold, m=sharp_m, s=sharp_s)

                generate_plot_fig(pictures, sharp_m, sharp_s, gui, face_col=themes[theme])
                plot_generated = True
            except UnboundLocalError:
                traceback.print_exc()
                
            



    return

    # gui.close()

    print('Generating picture instance list')
    pictures = generate_pictures(path)

    sharp_m = mean(pictures)
    sharp_s = std(pictures)


    print('Adding colour attribute')
    for p in pictures:
        img = p['instance']
        img.get_col(t=threshold, m=sharp_m, s=sharp_s)

    axes_data = format_axes(pictures)

    print('Files tagging')
    asyncio.run(tag_files(pictures))


    print('Drawing Plot')
    draw_plot(axes_data, sharp_m)

    
    print('DONE')



# main(path, threshold)

main()
    


# raise ValueError('A very specific bad thing happened.')