# LEDs_matrix_control

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/Altarax/LEDs_control">
    <img src="https://user-images.githubusercontent.com/46035021/141173582-9912054c-fa62-45d8-a8dd-a964239d683d.png" alt="Logo" width="160" height="160">
  </a>
</div>

## About the project

I wanted to create my own library by using a little bit of Python to control  
a matrix of leds. I'm using this matrix :
<div>
  <a href="https://github.com/Altarax/LEDs_control">
    <img src="https://m.media-amazon.com/images/I/71eB9U0mmFL._AC_SX569_.jpg" alt="Logo" width="160" height="160">
  </a>
</div>

## Some specifications

I had to create a tiny circuit to convert 3.3V to 5V to send data to the leds.
I bought it on JLPCB after using EASY EDA to create it :
<div>
  <a href="https://github.com/Altarax/LEDs_control">
    <img src="https://i.ibb.co/FX9ynXw/unnamed.png" alt="Logo" width="200" height="200">
  </a>
</div>

First of all, I'm using this code found here : http://stevenmerrifield.com/WS2812/index.html
Thanks to this person because I'll be able to do my first tests to understand the WS2812B correctly.

(05/12 : currently waiting the PCB)  
(02/01 : PCB finally here ! But I don't find my resistors...)  
(13/02 : Waiting for JTAG connector)  
(21/03 : Started the first tests and nothing is working)  
(24/05 : It's working ! Now I'll add another matrix and write a Python code to convert an image to a RGB matrix)  

## Roadmap

- [x] First tests 
- [ ] Python converter (Image -> RGB) 
- [ ] Create a package for the variable LED
- [ ] Create fonctions for LED (reset, add, modify)

## Me and programming langages (progression)
- *05/12/2021* 

| VHDL                        | Python                      | C                           |
|-----------------------------|-----------------------------|-----------------------------|
|  ➖➖➖➖➖🚀➖➖➖🌑  |  ➖➖➖➖➖➖🚀➖➖🌑  |  ➖➖➖➖➖➖🚀➖➖🌑  |
