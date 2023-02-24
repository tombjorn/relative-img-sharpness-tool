from modules import *
from gui import *
import asyncio
import sys
from tkinter.filedialog import askdirectory


def main():

    # threshold = float(sys.argv[1])
    # path = str(sys.argv[2])

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


# SHOULD DO A REGEX TEST TO MAKE SURE THRESH IS FLOAT AND DIR IS PATH
path = askdirectory(title='Select Folder')


threshold = float(input('Threshold: '))
while True:
    if isinstance(threshold, float) and 0.0 < threshold < 1.0:
        break
    try:
        threshold = float(input('Threshold: '))
    except ValueError:
        print('Threshold must be a float 0 - 1')

while True:
    print(f'Current Path = {path} \n')
    dir_choice = str(input(f'confirm image folder path? [y/n]\n'))
    if (dir_choice.lower() == 'y'):
        break
    path = askdirectory(title='Select Folder')

# main(path, threshold)
create_gui()

    


# raise ValueError('A very specific bad thing happened.')