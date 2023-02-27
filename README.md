
Short Description: 

App measures the relative sharpness of given images, tagging the resulting image files with a corresponding tag.


Long Description:

App measures the relative sharpness of a set of pictures, selected by directory.
Graphs the pictures based on this relative sharpness value, and given the app is on OSX, adds an appropriate colour tag to the files.
Sharpness measurement usually involves edge detection, often compared against a reference image. This algorithm instead crops the focus into the centre, by a factor of 0.25, in an attempt to circumvent interpretating a desired unfocused background, and only focusing on the center content. 
It then uses the gradient of gradients?


Run - python main.py  

References:

- "An Improved Method for Evaluating Image Sharpness Based on Edge Information",
  Zhaoyang Liu , Huajie Hong, Zihao Gan, Jianhua Wang and Yaping Chen,
  Applied Sciences.
  Source : https://www.mdpi.com/2076-3417/12/13/6712/pdf

TODO:
    - add mouse hover over graph points, index images by number, somehow able to open picture
        - could have a list selector to pick and open the picture by picture number in graph?
    - Figure out how to close with close red close button
    
    - Add more themes, find a way to access the whole theme array.
    - Add a method to move the focus of the algorithm