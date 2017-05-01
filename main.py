import pdb
import numpy as np
import cv2
import scipy.signal
import matplotlib.pyplot as plt
from math import pi
import rotate_crop_tool as rct


class Plaid():
    def __init__(self):
        self.length = 1000  # lower resolution if images taking too long to load
        self.clear_plaid()

    def add_sinusoid(self, frequency, orientation=0):
        """frequency is in cycles/cm. Orientation is in degrees ccw"""
        x = np.linspace(0, 2*pi*5, self.length*2)
        y = 255 * np.sin(x*(frequency*2))
        img = np.array([y]*self.length*2)
        (rows, cols) = np.shape(img)
        M = cv2.getRotationMatrix2D((cols/2, rows/2), orientation, 1)
        img_rotated = cv2.warpAffine(img, M, (cols, rows))
        img_rotated_cropped = rct.crop_around_center(img_rotated, self.length, self.length)
        self.cmp_wav_func += img_rotated_cropped

    def add_gauss_window(self, size=0.4):
        window_matrix_vert = np.array([scipy.signal.general_gaussian(1000, 1, size*(self.length-1)/2)] * self.length)
        (rows, cols) = np.shape(window_matrix_vert)
        M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
        window_matrix_horiz = cv2.warpAffine(window_matrix_vert, M, (cols, rows))
        self.cmp_wav_func = self.cmp_wav_func * window_matrix_vert * window_matrix_horiz
        
    def clear_plaid(self):
        self.cmp_wav_func = np.zeros([self.length, self.length])

    def show_plaid(self):
        plt.axis("off")
        plt.imshow(self.cmp_wav_func, cmap='gray')

    def crop_center(img, cropx, cropy):
        y, x = img.shape
        startx = x//2-(cropx//2)
        starty = y//2-(cropy//2)   
        return img[starty:starty+cropy, startx:startx+cropx]

    def shape(self):
        return self.cmp_wav_func.shape
    
p = Plaid()
p.add_sinusoid(0.5, 45)
p.add_sinusoid(100, 95)
p.add_sinusoid(4, 20)

p.add_gauss_window(size=0.35)

p.show_plaid()
