# Imports
from datetime import date
from enum import auto
from PIL import Image
import cv2
import numpy as np

# Global Variables
NB_OF_LEDS      = 256   #int
WEIGHT 			= 8     #int
HEIGHT			= 32    #int
IMAGE_NAME      = "marvel.png"    #string

DATE            = date.today()
AUTHOR          = "Jayson Dangremont"
MAIL            = "dangremontjayson.pro@gmail.com"
VERSION         = "1.0"

def create_pkg():
    file = open("led_ctrl_pkg.vhd", 'w')

    res = convert_image()
    res_grb = bgr_to_grb(res)

    print(res_grb)

    pixels = []

    for i in res_grb:
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
	--! Functions declarations
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
    img_bgr = cv2.imread(IMAGE_NAME)
    res = cv2.resize(img_bgr, dsize=(WEIGHT, HEIGHT), interpolation=cv2.INTER_NEAREST)
    return res

def bgr_to_grb(img_bgr):

    for i in img_bgr:
        for j in i:
            temp = j[0]
            j[0] = j[1]
            j[1] = j[2]
            j[2] = temp

    return img_bgr