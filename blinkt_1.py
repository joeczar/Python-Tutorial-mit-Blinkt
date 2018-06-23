# Das ist eine 'comment' und wird nicht interpretiert. Die sind da um den Code verstandlicher zu machen.

'''
das is ein multi-line 'comment'
Es wird auch nicht interpretiert
Hier können wir mehr Text und Info eingeben. 
'''

# install Blinkt von curl https://get.pimoroni.com/blinkt | bash

# als erstes mussen wir die Funktionen; set_pixel, set_brightness, show und clear von der blinkt Bibliotek importieren.

from blinkt import set_pixel, set_brightness, show, clear

# damit wir uns nicht blenden, setzten wir den Helligkeit runter. Helligkeit werte sind zwischen 1 und 0.1

set_brightness(0.1)

# um möglich beleuchtite LED's zu löschen benutzen wir clear()

clear()

'''
Jetzt kommt es zu die LEDs oder Pixels wie wir die ab jetzt nennen, mit der set_pixel Funktion.

Da es nur eine einzelne Reihe von acht Pixeln gibt, ist es einfach,
sie nacheinander zu durchlaufen, ihren Wert zu setzen und dann die Werte auf Blinkt anzuzeigen! mit der showFunktion.

set_pixel wird mit 4 Argumente übergeben, - x, r, g und b.

set_pixel(x, r, g, b)

x ist der Pixelposition. wir haben 8 Pixels aber die mit werten von 0-7 ansprechen.
r, g, und b, sind die RGB-Farbwerte.

Im RGB-Farbsystem hat jede Farbe einen Wert zwischen 0 und 255, was bedeutet, dass 255,255,255 weiß und 0,0,0 schwarz ist.
Daraus folgt, dass 255,0,0 rot ist, 0,255,0 grün ist und so weiter.
'''
# Beachten Sie, dass die Pixel wie in Python von 0 bis 7 indiziert sind und nicht von 1 bis 8, so dass das Pixel ganz links Index 0 ist.

set_pixel(0, 255, 255, 255)

# Als letztes mussen wir die Pixels an schalten mit show()

show()


# wie können wir eine andere Pixel jetzt beleuchten? und eine andere Farbe? Wie schalte ich den Pixel aus?
