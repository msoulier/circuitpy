from adafruit_circuitplayground.express import cpx
import time

cpx.pixels.brightness = 0.1

MAX_COLOURS = 3
COLOURS = [
    [ 0xFF0000, 0x00FF00, 0x0000FF ],
    [ 0xDD0000, 0x00DD00, 0x0000DD ],
    [ 0xBB0000, 0x00BB00, 0x0000BB ],
    [ 0x990000, 0x009900, 0x000099 ],
    [ 0x770000, 0x007700, 0x000077 ],
    [ 0x550000, 0x005500, 0x000055 ],
    [ 0x330000, 0x003300, 0x000033 ],
    [ 0x110000, 0x001100, 0x000011 ],
]

PIXEL_TICK_INTERVAL = 0.1
MAX_PIXEL_TICKS = 7
MAX_PIXELS = 10

current_pixel = 0
pixels = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
]

while 1:
    time.sleep(PIXEL_TICK_INTERVAL)
    pixels[current_pixel] = MAX_PIXEL_TICKS
    for i in range(MAX_PIXELS):
        pixels[i] -= 1
        if pixels[i] > 0:
            cpx.pixels[i] = COLOURS[MAX_PIXEL_TICKS - pixels[i]][i % MAX_COLOURS]
            continue
        cpx.pixels[i] = 0
    current_pixel += 1
    current_pixel %= MAX_PIXELS
