# Imports
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
IMAGE_PATH      = "Image/marvel.png"
RESIZE_NEEDED   = True
DATE            = date.today()
AUTHOR          = "Jayson Dangremont"
MAIL            = "dangremontjayson.pro@gmail.com"
VERSION         = "1.0"

def create_pkg():
    file = open("Generated_VHDL/led_ctrl_pkg.vhd", 'w')
    image = convert_image()    
    image_grb = bgr_to_grb(image)
    pixels = create_good_pattern(image_grb)

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

def create_good_pattern(image_grb):
    """
    w = Width
    p = Pixel
    h = Height

    Matrix returned by opencv is like this : [P1][P2][P3]...[Ph]
    But, the components on the matrix are cabled like this :
    [P1][Pw+8][Pw+9]
    [P2][Pw+7][Pw+10]
    .   .     .
    .   .     .  
    .   .     . 
    [Pw][Pw+1][Pw+16]
    It's from top to bottom, bottom to top and so on. So, the next algo has been created
    in order to match the pattern with the good pattern sent by FPGA.
    """
    pixels = []
    temp_list = []
    even = 0

    for i in range(32):
        if even == 0:
            for j in range(8):
                pixels.append(rgb_to_hex_vhd(tuple(p for p in image_grb[j][i])))
                even = 1
        else:
            for j in range(8):
                temp_list.append(rgb_to_hex_vhd(tuple(p for p in image_grb[j][i])))

            for p in reversed(temp_list):
                pixels.append(p)

            temp_list.clear()
            even = 0  
            
    return pixels

def rgb_to_hex_vhd(rgb):
    return 'X"%02X%02X%02X"' % rgb

def convert_image():
    image_base = cv2.imread(IMAGE_PATH)

    if not(len(image_base) > WIDTH*HEIGHT) and not(RESIZE_NEEDED):
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