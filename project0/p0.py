#-------------------------------------
#| Pattern-maker (Project 0)
#| Created on 5/30/14
#| Written by Blair Kiel for CS250
#-------------------------------------

import sys

def main():

    height = int(sys.argv[1])
    if (height > 1280):
        print("The image must be at most 1280 pixels high!", file=sys.stderr)
        return None
    width = height* 2
    print_ppm(height,width)
    return

def print_ppm(height,width):

    print("P3")
    print(str(width) + ' ' + str(height))
    print("255")
    redbound = 0
    bluebound = height
    whiteone = height
    whitetwo = width-1
    for y in range(0, height):
        red = "255 0 0 "
        green = "0 255 0 "
        blue = "0 0 255 "
        white = "255 255 255 "
        for x in range(0, width):

            if(x == whiteone):
                print(white)
                whiteone = whiteone - 1
            elif(x == whitetwo):
                print(white)
                whitetwo = whitetwo - 1
            elif(x <= redbound):
                print(red)
            elif(x >= bluebound):
                print(blue)
            else: 
                print(green)
        redbound = redbound + 1
        bluebound = bluebound + 1
    return

main()


