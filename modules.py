import os
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
import macos_tags as mt



Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


# build array of pictures, might change data structure
#TODO - Refactor to regex if easier? or select from array of extensions?
def generate_pictures(img_folder_path):

    pictures = []

    for file in os.listdir(img_folder_path):
        filename = os.fsdecode(file)
        if filename.endswith(".JPG") or filename.endswith(".png") or filename.endswith(".jpg"):
            path = os.path.join(f'{img_folder_path}/{filename}')
            try:
                p = Picture(path)
                container = {'filepath' : path, 'sharpness' : p.sharpness, 'instance' : p}
                pictures.append(container)

            except Image.DecompressionBombWarning:
                        print('error')
        else:
            continue
    return pictures

def mean(arr):
    return np.mean([p['sharpness'] for p in arr])

def std(arr):
    return np.std([p['sharpness'] for p in arr])

def format_axes(pictures):
    x = []
    y = []
    col = []
    for idx, p in enumerate(pictures):
        picture = p['instance']
        x.append(idx)
        y.append(picture.sharpness)
        col.append(picture.colour)
    return {'x':x, 'y':y, 'col':col}


def draw_plot(data, mean):
    plt.title('Relative Sharpness')
    plt.scatter(x=data['x'], y=data['y'], c=data['col'])
    plt.axhline(y=mean, c='black', linestyle='dashed')
    plt.xlabel("No.", fontweight='bold', c='orange')
    plt.ylabel("Relative Sharpness", fontweight='bold', c='red')
    plt.show()

async def tag_files(pictures):
    for p in pictures:
        img = p['instance']
        img.tag_me()

def cli_error():
    print('\n')
    print('Please Enter correct number of arguments!')
    print('\n')
    print('For help run - python main.py help')
    print('\n')

def get_help():
    print('\n')
    print('---- HELP ----')
    print('\n')
    print('CLI - python main.py "threshold" "directory"')
    print('\n')
    print('Threshold - Float, 0-1')
    print('\n')
    print('Directory - The folder path containing the images to analyse')
    print('\n')
                
class Picture():
    def __init__(self, filepath):
        self.filepath = filepath
        self.sharpness = self.get_sharpness(self.filepath)
    
    def get_sharpness(self, img_path):
        img = Image.open(img_path).convert('L')

        image_arr = np.asarray(img, dtype=np.int32)

        # crop to center
        xDist, yDist = image_arr.shape
        xStart, xEnd, yStart, yEnd = self.define_edges(xDist, yDist)
        array = image_arr[yStart:yEnd, xStart:xEnd]

        # continue with gradient
        gy, gx = np.gradient(array)
        gnorm = np.sqrt(gx**2 + gy**2)
        sharpness = np.average(gnorm)
        return sharpness
    
    def define_edges(self, xDist, yDist):
        xStart = math.floor(xDist * 0.25)
        xEnd = math.floor(xDist * 0.75)
        yStart = math.floor(yDist * 0.25)
        yEnd = math.floor(yDist * 0.75)
        return xStart, xEnd, yStart, yEnd

    def get_col(self, **options):
        mean = options['m']
        std = options['s']
        thresh = options['t']
        if (self.sharpness > ((mean + std) * thresh)):
            self.colour = 'green'
        elif (self.sharpness >= mean):
            self.colour = 'orange'
        else: self.colour = 'red'

    def tag_me(self):
        tag_1 = mt.Tag(name="Sharpest", color=mt.Color.GREEN)
        tag_2 = mt.Tag(name="Sharp", color=mt.Color.YELLOW)
        tag_3 = mt.Tag(name="Not Sharp", color=mt.Color.RED)
        if self.colour == 'green':
            mt.add(tag_1, file=self.filepath)
        elif self.colour == 'orange':
            mt.add(tag_2, file=self.filepath)
        else:
            mt.add(tag_3, file=self.filepath)



            
        
