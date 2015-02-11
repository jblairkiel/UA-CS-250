import sys

def main():

    height = int(sys.argv[1])
    width = height * 2
    print("P3")
    print(str(width) + ' ' + str(height))
    print("255")
    ppm(height)
    return

def ppm(height):

    red = "255 0 0 "
    green = "0 255 0 "
    blue = "0 0 255 "
    white = "255 255 255 "
    half = int(height/2)
    rednum = 1
    greennum = height-1
    bluenum = height-1
    for i in range(0, height):

        for j in range(0, rednum):
            print(red)
        print(white)
        for k in range(1,greennum):
            print(green)
        print(white)
        for l in range(0,bluenum):
            print(blue)

        rednum = rednum + 1
        bluenum = bluenum - 1
    return

main()

        
