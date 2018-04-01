from tkinter import mainloop
import math

from usefull import WIDTH, HEIGHT, get_img


def traditional(radius, auto_delete=False, auto_time=None):

    img = get_img("traditional", auto_delete, auto_time)
    for x in range(-radius, radius):

        # Changing coordinates as origin is at bottom left of sceen
        z = int(x + WIDTH/2)
        w = math.sqrt(abs(x**2 - radius**2))

        # Draw under and above x-changed (or z) axis
        img.put("#ffffff", (z, int(HEIGHT/2 + w)))
        img.put("#ffffff", (z, int(HEIGHT/2 - w)))

    mainloop()
