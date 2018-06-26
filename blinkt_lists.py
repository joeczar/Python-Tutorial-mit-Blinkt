# Python Listen https://py-tutorial-de.readthedocs.io/de/python-3.3/introduction.html#listen

'''
In Python eine Liste ist eine von viele möglichkeit von viele um unterschiedlicher Werte zu gruppieren.
Wir werden Listen benutzen um RGB-Farbwerte zu speichern.

Um eine liste zu machen brauchen wir ein Variable um die zu Speichern.

Lass uns mit rot anfangen. Eine liste von Werten (unsere RGB werte) wird von Kommas getrennt und von eckigen Klammern eingeschlossen.

rot = [255, 0, 0]

Vor wir den nutzen kann mussen wir den deklariern. Das heisst es soll vor der auszuführender Code platziert werden.

Um die Liste in unsere set_pixel Funktion zu benutzen, mussen wir die einzelne werte daraus ziehen.

Listen sind 0 indexiert. Das heißt, wenn wir 3 werten haben wir mussen die von 0-2 aufzehlen.

rot[0]
rot[1]
rot[2]

So können wir unsere RGB Werten damit ersetzen.

Probiere es jetzt aus. Danach mache eine für Grün, Blau, Gelb und Magenta.
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
