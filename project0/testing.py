import sys
from random import randint

def main():

    height = int(sys.argv[1])
    width = height * 2
    ppm(height,width)
    return

def ppm(height,width):

    print("P3")
    print(str(width) + ' ' + str(height))
    print("255")
    red = "255 0 0 "
    redbound = 0
    bluebound = height
    whiteone = height
    whitetwo = width-1
    for y in range(0, height):
        for x in range(0, width):
            red = "255 0 0 "
            green = "0 255 0 "
            blue = "0 0 255 "
            white = "255 255 255 "
            color = (randint(0,255),randint(0,255),randint(0,255))
            print(color)
    return

main()


