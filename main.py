import pdb
from math import sin,pi
import numpy as np
import cv2

class Plaid():
    def __init__(self):
        self.resolution = 1000 # lower resolution if images taking too long to load
        self.square_length = int(sqrt(2*self.resolution**2))
        self.clear_plaid()
        
    def add_sinusoid(self, frequency, orientation = 0):  ## frequency is in cycles/cm. Orientation is in degrees ccw
        x = np.linspace(0, 2*pi*5, self.square_length)
        y = 127 * np.sin(x*(frequency*2))
        img = np.array([y]*self.square_length)
        pdb.set_trace()
        (rows, cols) = shape(img)
        M = cv2.getRotationMatrix2D((cols/2,rows/2),orientation,1)
        self.cmp_wav_func += cv2.warpAffine(img,M,(cols,rows))
        
    def clear_plaid(self):
        self.cmp_wav_func = np.zeros([self.square_length, self.square_length])
        
    def show_img(self):
        imshow(self.cmp_wav_func, cmap='gray')

w = Wave()
w.add_sinusoid(0.5, 90)
w.add_sinusoid(2, 0)
w.show_img()
