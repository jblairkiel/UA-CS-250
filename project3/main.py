########################
#Project 2 by Blair Kiel
#Requires sys and scanner
#I have tried to test every
#usable aspect of my project
#
#It also requires input files from the
#command line.
#######################
from image import PortablePixmap
from image import Color
from image import *
import sys
from scanner import *

def main():
    #Test for valid image
    method = sys.argv[1]
    image = sys.argv[2]
    a = read_ppm(image)
    if(method == 'grayscale'):
        a.grayscale()
    elif(method == 'flip'):
        a.flip()
    elif(method == 'flop'):
        a.flop()
    a.__str__()
    #print("Magic number: Should be P3")
    #print(a.magicNum)
    #print("Width: Should be 2X the height")
    #print(a.width)
    #print("Height: Should be the height of the document")
    #print(a.height)
    #print("Maximum number of colors: Should be 255")
    #print(a.maxVal)
    #print("Pixel Data: Should print an array of the arrangement of pixels")
    #print(a.pixelData)

    #Not sure what values we need to test for
    #so i put random values
    #c = Color(125, 30, 40)
    #print("pixel: Should display the RGB values to create a single pixel")
    #print(c.pixel)
    #print("getRed(): Should return the first parameter")
    #print(c.getRed())
    #print("getGreen(): Should return the second parameter")
    #print(c.getGreen())
    #print("getBlue(): Should return the third parameter")
    #print(c.getBlue())

    #This is the test to see if there is a invalid image file
    #and will catch an error

    #image2 = sys.argv[2]
    #print("If loaded with a file with too many or too few pixels, will thrown an error")
    #b = read_ppm(image2)

main()
