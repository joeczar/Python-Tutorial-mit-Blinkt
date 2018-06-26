from blinkt import set_pixel, set_brightness, show, clear
import time

rot = [255, 0, 0]
grün = [0, 255, 0]
blau = [0, 0, 255]
cyan = [0, 127, 127]
magenta = [127, 0, 127]
gelb = [127, 127, 0]
schwarz = [0, 0, 0]

farbe = [0, 0, 0]

farben = [rot, grün, blau, cyan, magenta, gelb, schwarz]

set_brightness(0.1)

for i in range(len(farben)):
    clear()
    farbe = farben[i]
    set_pixel(0, farbe[0], farbe[1], farbe[2])
    show()
    time.sleep(0.5)
