import sys
from scanner import *

class PortablePixmap():

    def __init__(self, magicNum, width, height, maxVal, pixelData):

        self.magicNum = magicNum
        self.width = width
        self.height = height
        self.maxVal = maxVal
        self.pixelData = pixelData

    def pixelString():
        
        self.string = self.magicNum + " " + self.width + " " + self.height + " " + self.maxVal + " " + self.pixelData 

class Color():

    def __init__(self, redval, greenval, blueval):
        
        self.redval = redval
        self.blueval = blueval
        self.greenval = greenval
        self.pixel = [redval, greenval, blueval]

    def getRed(self):

        return self.pixel[0]

    def getGreen(self):

        return self.pixel[1]

    def getBlue(self):

        return self.pixel[2]

def read_ppm(filename):

        with open(filename, 'r') as f:
            data = f.readlines()
            pmap = []

            for token in data:
                words = token.split()
                pmap.append(words)
            f.close()

        magicNum = pmap[0]
        width = pmap[1][0]
        height = pmap[1][1]
        maxVal = pmap[2]
        pixelData = pmap[3:]
        if (len(pixelData) == int(width) * int(height)):
            counter = True
        else:
            print("The file has an incorrect pixel height or width according to the pixel data")
            sys.exit()
        for i in range(0,len(pixelData)):
            if ((len(pixelData[i])) % 3 == 0):
                counter = True
            else:
                print("The file has an incorrect number of values to make a valid pixel. Ex (0, 0, 255)")
                sys.exit()
        return PortablePixmap(magicNum, width, height, maxVal, pixelData)

        
        #I found a better way to catch errors
        #try:
        #    len(pixelData) == 3 
        #except ValueError:
        #    print("There is a problem with your ppm data")
