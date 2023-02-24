from modules import *
from gui import *
import asyncio
import sys
from tkinter.filedialog import askdirectory

LightBrown7 = {"main" : '#f6c89f', 
               "sec" : '#396362',
               "acc" : '#f7f9f9'}

def main():
    plot_generated = False
    threshold = float(sys.argv[1])
    gui = create_gui()

    # print(f'_VARS RETURNED FROM CREATE_GUI() :{gui}')

    while True:
        print(f'_VARS INSIDE WHILE LOOP: {gui}')

        event, values = gui['window'].read(timeout=200)
        if event == 'EXIT':
            print('exit event')
            break

        if event == "PICK A FOLDER":
            path = askdirectory(title='Image directory')
            gui['window']['DIR PATH'].update(f'DIRECTORY PATH : {path}')

        if event == "SHOW PLOT" and plot_generated == False:
            print('Generating picture instance list')
            pictures = generate_pictures(path)
            sharp_m = mean(pictures)
            sharp_s = std(pictures)
            for p in pictures:
                img = p['instance']
                img.get_col(t=threshold, m=sharp_m, s=sharp_s)

            axes_data = format_axes(pictures)
            generate_plot_fig(axes_data, sharp_m, sharp_s, gui, face_col=LightBrown7)
            plot_generated = True


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