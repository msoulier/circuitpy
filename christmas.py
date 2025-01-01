from adafruit_circuitplayground.express import cpx
import time

interval = 0.1
brightness = 0.5
current_pixel = 0
max_pixels = 10
cpx.pixels.brightness = brightness

GREEN = 0x00FF00
RED = 0xFF0000
BLUE = 0x0000FF
BLACK = 0x000000

colours = (GREEN, RED, BLUE)
current_colour = 0

while True:
    cpx.pixels[current_pixel] = colours[current_colour]
    time.sleep(interval)
    cpx.pixels[current_pixel] = BLACK
    current_pixel += 1
    current_pixel %= max_pixels
    current_colour += 1
    current_colour %= 3
