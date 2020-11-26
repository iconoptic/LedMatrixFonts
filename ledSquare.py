#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
import arial


# LED strip configuration:
LED_COUNT      = 128      # Number of LED pixels.
LED_PIN        = 18# GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
COLS           = int(LED_COUNT/8)


colors = {
        "red" : Color(255,0,0),
        "orange" : Color(255,91,0),
        "yellow" : Color(255,230,0),
        "green" : Color(43,255,0),
        "cyan" : Color(0,255,187),
        "blue" : Color(0,0,255),
        "purple" : Color(111,0,255),
        "pink" : Color(255,0,255),
        "magenta" : Color(255,0,144),
        "white" : Color(255,255,255)
}
cNums = [colors["red"],colors["orange"],colors["yellow"],colors["green"],colors["cyan"],colors["blue"],colors["purple"],
            colors["pink"],colors["magenta"],colors["white"]]

screen = []
for i in range(8):
    screen.append([])
    flip = True
    for j in range(COLS):
        if flip:
            screen[i].append(j*8+i)
            flip = False
        else:
            screen[i].append(j*8+(7-i))
            flip = True
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).

strip.begin()

def get (x, y):
    return int(screen[x][y])

def plot (x, y):
    strip.setPixelColor(get(x,y), Color(255,255,255))
    strip.show()

def plotColor (x, y, color):
    strip.setPixelColor(get(x,y), color)
    strip.show()

def picture (arr, color, xOff, yOff):
    pix = []
    ###change to array of booleans
    if type(arr[0][0]) is int:
        for i in range(len(arr)):
            for j in range(len(i)):
                if arr[i][j] == 0: arr[i][j] = False
                else: arr[i][j] = True
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]:
                if j+xOff < COLS:
                    pix.append(screen[i+yOff][j+xOff])
    for i in pix:
        strip.setPixelColor(i, color)
    strip.show()
        #time.sleep(0.25)
    #strip.show()

def clear():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()
                    
def shStr (inStr):
    clear()
    letters = []
    for i in inStr:
        print(ord(i)-1)
        for s in arial.font[ord(i)-1]:
            print(s)
        letters.append(arial.font[ord(i)-1][2:])

    out = []
    for i in range(8): out.append([])
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            for k in range(len(letters[i][j])):
                if i < 9: out[j].append(letters[i][j][k])
    for i in out:
        print(i)
    out.remove([])
    for i in range(len(out[0])):
        picture([out[0][i:COLS+i],out[1][i:COLS+i],out[2][i:COLS+i],out[3][i:COLS+i],out[4][i:COLS+i]], Color(255,255,255), -COLS, 8-len(out))
        if i == 0:
            time.sleep(1)
        time.sleep(0.1)
        clear()


"""
           [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
            ]
"""


####################    Part of example
def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
####################    
