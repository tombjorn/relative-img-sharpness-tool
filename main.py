from modules import *
import asyncio
import sys

def main():

    threshold = float(sys.argv[1])
    path = str(sys.argv[2])

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
if len(sys.argv) == 1:
    cli_error()
elif sys.argv[1] == 'help':
    get_help()
else:
    main()
    


# raise ValueError('A very specific bad thing happened.')