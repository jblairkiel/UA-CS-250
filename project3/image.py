import sys
from scanner import *

class PortablePixmap():

    def __init__(self, magicNum, width, height, maxVal, pixelData):

        self.magicNum = magicNum
        self.width = width
        self.height = height
        self.maxVal = maxVal
        self.pixelData = pixelData
        return

    def __str__(self):

        return print(self.magicNum[0]), print(str(self.width + " " + self.height)),  print(self.maxVal[0]), print(self.pixelData)

    def flip(self):

        str(PortablePixmap)
        self.list1 = []
        self.list2 = []
        self.list3 = []
        for j in range(0, len(self.pixelData)-1):
            self.list1.append(self.pixelData[j])
            if (len(self.list1) == int(self.width)):
                self.list2.append(self.list1)
                self.list1 = []
        self.list2.reverse()
        self.pixelData = self.list2
#        for i in range(0, len(self.list2)):
#            for j in range(0, len(self.list2[i])):
#                pix = str(str(self.list2[i][j][0]) + " " + str(self.list2[i][j][1]) + " " + str(self.list2[i][j][2]))
#                self.list3.append(pix)
        return

    def flop(self):
        self.list3 = []
        self.list4 = []
        self.list5 = []
        for j in range(0, len(self.pixelData)):
            self.list3.append(self.pixelData[j])
            if (len(self.list3)== int(self.width)):
                self.list3.reverse()
                self.list4.append(self.list3)
                self.list3 = []
        self.pixelData = self.list4
        str(PortablePixmap)
        #for i in range(0, len(self.list4)):
        #    for j in range(0, len(self.list4[i])):
        #        pix = str(str(self.list4[i][j][0]) + " " + str(self.list4[i][j][1]) + " " + str(self.list4[i][j][2]))
        #        self.list5.append(pix)
        #self.pixelData = self.list5
        #str(PortablePixmap)
        return

    def grayscale(self):
        self.list5 = []
        print(self.magicNum[0])
        print(str(self.width + " " + self.height))
        print(self.maxVal[0])
        for j in range(0, len(self.pixelData)):
            c = Color(self.pixelData[j])
            grayPix = round(.2126* int(c.getRed()) + round(.7152 * int(c.getGreen())) + round(.0722 * int(c.getBlue()))) 
            #grayPix = str(round(.2126 * int(c.getRed())))+ " " + str(round(.7152 * int(c.getGreen())))+ ' ' + str(round(.0722 * int(c.getBlue())))
            grayArray = [str(grayPix) + " " + str(grayPix) + " " +str(grayPix)]
            self.list5.append(grayArray)
        self.pixelData = self.list5
        str(PortablePixmap)
        return

class Color():

    def __init__(self, pixel):
        
        self.pixelChange = pixel

    def getRed(self):

        return self.pixelChange[0]

    def getGreen(self):

        return self.pixelChange[1]

    def getBlue(self):

        return self.pixelChange[2]

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
