sinwave = []
import math, numpy as np, board, neopixel, time, sys, random


pixel_pin = board.D18
ORDER = neopixel.GRB
# The number of NeoPixels
num_pixels = 60

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)
def mixrgb(rgb1, rgb2, factor):
    return round(rgb1[0]*factor + rgb2[0]*(1-factor)), round(rgb1[1]*factor + rgb2[1]*(1-factor)), round(rgb1[2]*factor + round(rgb2[2]*(1-factor)))
def sigmoid(x):
    return 1/(1 + np.exp(x))

   
def Sigma(rgb1, rgb2, TimeStep):
    step=0

    while sigmoid(num_pixels+num_pixels/12+step)<0.99:
        
        step-=0.1
        for y in range(num_pixels):
            pixels[y]=mixrgb(rgb2,rgb1,sigmoid(y+5+step))
        time.sleep(TimeStep)
        pixels.show()
        
def Fate(rgb1, rgb2, TimeStep):
    step=0
    for x in range(len(pixels)):
        pixels[x]=rgb1
    while not pixels[0]==rgb2:
        for x in range(len(pixels)):
            pixels[x]=mixrgb(rgb2,rgb1,sigmoid(5+step))
        step-=0.1
        time.sleep(TimeStep)
        pixels.show()

s1 = int(sys.argv[1])
s2 = int(sys.argv[2])
s3 = int(sys.argv[3])
s4 = int(sys.argv[4])
s5 = int(sys.argv[5])
s6 = int(sys.argv[6])
    
if(bool(random.getrandbits(1))):  
    Fate([s1, s2, s3], [s4,s5,s6], 0.005)
else:
    Sigma([s1, s2, s3], [s4,s5,s6], 0.005)
    



