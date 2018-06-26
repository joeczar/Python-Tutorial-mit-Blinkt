# Python Listen https://py-tutorial-de.readthedocs.io/de/python-3.3/introduction.html#listen

'''

'''

from blinkt import set_pixel, set_brightness, show, clear

rot = [255, 0, 0]
grün = [0, 255, 0]
blau = [0, 0, 255]
cyan = [0, 255, 255]
magenta = [255, 0, 255]
gelb = [255, 255, 0]

farbe = gelb

set_brightness(0.1)

clear()

set_pixel(0, farbe[0], farbe[1], farbe[2])

show()
