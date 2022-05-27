# Imports
from datetime import date
from enum import auto
from PIL import Image
import cv2
import numpy as np

# Global Variables
NB_OF_LEDS      = 256   #int
WEIGHT 			= 8		#int
HEIGHT			= 32	#int
IMAGE_NAME      = "marvel.png"    #string

DATE            = date.today()
AUTHOR          = "Jayson Dangremont"
MAIL            = "dangremontjayson.pro@gmail.com"
VERSION         = "1.0"

def convert_image():
    img = cv2.imread(IMAGE_NAME)
    res = cv2.resize(img, dsize=(WEIGHT, HEIGHT), interpolation=cv2.INTER_CUBIC)

    return res

def create_pkg():
    file = open("led_ctrl_pkg", 'w')

    res = convert_image()

    pixels = []

    for i in res:
        for j in i:
            for length in range(0, len(j), 3):
                pixels.append(rgb_to_hex_vhd(tuple(j[length:length+3])))

    file.write(
        f'''
--! \\file led_matrix_ctrl_pkg.vhd
--!
--! \\brief Package to control leds matrix.
--!
--! \\version {VERSION}
--! \\date {DATE}
--!
--! \\author {AUTHOR}, {MAIL}

--! Use standard library.
library IEEE;

--! Use logic elements library.
use IEEE.STD_LOGIC_1164.ALL;

    constant LED : LED_matrix_type := (
        '''
    )

    count = 0
    for p in pixels:
        if count == 0:
            file.write("\t\t\t")

        count += 1
        file.write(p + ", ")

        if count == 5:
            file.write("\n")
            count = 0

    file.write(")")

    file.close()

def rgb_to_hex_vhd(rgb):
    return 'x"%02x%02x%02x"' % rgb