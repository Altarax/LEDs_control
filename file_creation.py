# Imports
from audioop import reverse
from datetime import date
from email.mime import image
from enum import auto
from PIL import Image
import cv2
import numpy as np

# Global Variables
NB_OF_LEDS      = 256         
WIDTH 			= 8             
HEIGHT			= 32            
IMAGE_NAME      = "marvel.png"   

DATE            = date.today()
AUTHOR          = "Jayson Dangremont"
MAIL            = "dangremontjayson.pro@gmail.com"
VERSION         = "1.0"

def create_pkg():
    file = open("led_ctrl_pkg.vhd", 'w')
    image = convert_image()    
    image_grb = bgr_to_grb(image)
    
    pixels = []

    temp_list = []
    odd = 0
    for i in range(32):
        if odd == 0:
            for j in range(8):
                pixels.append(rgb_to_hex_vhd(tuple(p for p in image_grb[j][i])))
                odd = 1
        else:
            for j in range(8):
                temp_list.append(rgb_to_hex_vhd(tuple(p for p in image_grb[j][i])))

            for p in reversed(temp_list):
                pixels.append(p)

            temp_list.clear()
            odd = 0   

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

library IEEE;
use IEEE.STD_LOGIC_1164.all;

package led_ctrl_package is

	--! Custom types
	type LED_matrix_type is array (0 to 255) of std_logic_vector(23 downto 0);
	
	--! Main variable created by python file
	constant LED : LED_matrix_type := (
        '''
    )

    count = 0
    for p in range(len(pixels)):
        if count == 0:
            file.write("\t\t\t")

        count += 1
        if p != len(pixels)-1:
            file.write(pixels[p] + ", ")
        else:
            file.write(pixels[p])

        if count == 10:
            file.write("\n")
            count = 0

    file.write(");")

    file.write('''
	\n\t--! Functions declarations
	function reset_matrix(matrix : in LED_matrix_type) return LED_matrix_type;
	
end package led_ctrl_package;

package body led_ctrl_package is

	-- Functions implementations
	function reset_matrix(matrix : in LED_matrix_type) return LED_matrix_type is
		variable temp_matrix : LED_matrix_type := matrix;
	begin
		for i in 0 to (matrix'length-1) loop
			temp_matrix(i) := x"000000";
		end loop;
		return temp_matrix;
	end function;

end package body led_ctrl_package;
    ''')

    file.close()

def rgb_to_hex_vhd(rgb):
    return 'X"%02X%02X%02X"' % rgb

def convert_image():

    image_base = cv2.imread(IMAGE_NAME)

    if not(len(image_base) > WIDTH*HEIGHT):
        return image_base
    else:
        image_base = cv2.resize(image_base, dsize=(HEIGHT, WIDTH), interpolation=cv2.INTER_NEAREST)
        return image_base

def bgr_to_grb(img_bgr):

    for i in img_bgr:
        for j in i:
            temp = j[0]
            j[0] = j[1]
            j[1] = j[2]
            j[2] = temp

    return img_bgr