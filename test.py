from cv2 import imread
import cv2

IMAGE_NAME      = "test.png"   

file = open("led_ctrl_pkg.vhd", 'w')
img = cv2.imread(IMAGE_NAME)

def rgb_to_hex_vhd(rgb):
    return 'X"%02X%02X%02X"' % rgb

odd = 0
pixels = []
temp = []
temp_list = []
for i in range(32):
    if odd == 0:
        for j in range(8):
            pixels.append(rgb_to_hex_vhd(tuple(i for i in img[j][i])))
            odd = 1
    else:
        for j in range(8):
            temp.append(rgb_to_hex_vhd(tuple(i for i in img[j][i])))
            odd = 0
        pixels.append(temp[::-1])

print(pixels)