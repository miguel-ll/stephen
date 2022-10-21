#from PIL import Image
#import pytesseract
#import numpy as np
import os

def speak(txt):
    os.system(f'espeak -s 110 "{txt}" > /dev/null 2>&1')

# another feature?
#def speak2()

"""
def rdimg(fname):
    img1 = np.array(Image.open(fname))
    text = pytesseract.image_to_string(img1)
    speak(text)
#rdimg(fname)
"""
