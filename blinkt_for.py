from blinkt import set_pixel, set_brightness, show, clear
import time

rot = [int(255), int(0), int(0)]
grün = [int(0), int(255), int(0)]
blau = [int(0), int(0), int(255)]
cyan = [int(0), int(127), int(127)]
magenta = [int(127), int(0), int(127)]
gelb = [int(127), int(127), int(0)]
schwarz = [int(0), int(0), int(0)]

farbe = [int(0), int(0), int(0)]



r = 0
g = 0
b = 0

farben = [rot, grün, blau, cyan, magenta, gelb, schwarz]

set_brightness(0.1)

for i in range(len(farben)):
    clear()
    farbe = farben[i]
    set_pixel(0, farbe[0], farbe[1], farbe[2])
    show()
    time.sleep(0.5)
