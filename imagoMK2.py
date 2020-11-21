import cv2
import numpy as np


ASCII_CHARS = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', 
    '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 
    'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 
    'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't',
    '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']',
    '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', 
    ';', ':', ',', '"', '^', '`', '.']


def img_to_ascii(image, w, h):
    pass


def main():
    
    IMAGE_PATH = input('Please enter the image path: ')
    IMAGE_WIDTH = input('Please select the width: ')
    IMAGE_HEIGHT = input('Please select the height: ')

    try:
        img = cv2.imread(IMAGE_PATH)
    except:
        print(IMAGE_PATH, "is not a valid path name to an image.")

    img_to_ascii(img, IMAGE_WIDTH, IMAGE_HEIGHT)
    
    # with open("ascci_image.txt", "w") as f:
    #     f.write(ascii_image)