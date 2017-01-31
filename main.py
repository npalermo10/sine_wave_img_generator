from math import sin,pi
import numpy as np


class Wave():
    def __init__(self):
        self.resolution = 1000 # lower resolution if images taking too long to load
        self.clear_function()
        
    def add_sinusoid(self, frequency):  ## frequency is in cycles/cm but it would be better to measure as cycles per degree.
        x = np.linspace(0, 2*pi*5, self.resolution)
        y = 128 * np.sin(x*(frequency*2)) + 128
        self.cmp_wav_func += y

    def clear_function(self):
        self.cmp_wav_func = np.zeros(self.resolution)
        
    def show_img(self):
        img = [self.cmp_wav_func]*self.resolution
        imshow(img, cmap='gray')
