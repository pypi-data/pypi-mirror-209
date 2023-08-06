# PyTraffic - Init

''' This is the __init__.py file. '''

# Imports
import os

# Variables
tesseractPath = None

# Function 1 - Init
def init():
    global tesseractPath

    if (os.path.exists("C:/Program Files/Tesseract-OCR/tesseract.exe")):
        tesseractPath = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    elif (os.path.exists("C:/Program Files (x86)/Tesseract-OCR/tesseract.exe")):
        tesseractPath = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
    else:
        tesseractPath = "Path Not Found"