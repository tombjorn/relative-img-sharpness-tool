App measures the relative sharpness of a set of pictures, selected by directory.
Graphs the pictures based on this relative sharpness value, and given the app is on OSX, adds an appropriate colour tag to the files.

Run - python main.py threshold 'image-folder-path' 

threshold - float 0-1

image-folder-path - path of folder containing images to analyse, cannot be sibling directory

References:

- "An Improved Method for Evaluating Image Sharpness Based on Edge Information",
  Zhaoyang Liu , Huajie Hong, Zihao Gan, Jianhua Wang and Yaping Chen,
  Applied Sciences.
  Source : https://www.mdpi.com/2076-3417/12/13/6712/pdf
