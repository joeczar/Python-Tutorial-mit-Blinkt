from blinkt import set_pixel, set_brightness, show, clear
import time

while True:
    clear()
    set_pixel(0, 255, 0, 0)
    show()
    time.sleep(0.5)
    clear()
    show()
    time.sleep(0.5)
