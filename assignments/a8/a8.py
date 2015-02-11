import sys
import string
from scanner import *

class Decode():

    def __init__(self):

        self.secret = []
        return

    def __str__(self):
        
        return print("Shhh! The secret message is:"),  print(str(self.secret))

    def decoder(self):

        code = sys.argv[1]
        self.readIn(code)

        return

    def decodeEngine(self,magicNum, audioData, twoNum):

        counter = 0
        counter2 = 0
        binaryList = []
        condensedList = []
        condensedList2 = []
        for i in range(0, len(audioData) - 1):
            counter = counter + 1
            if(counter == magicNum):
                binaryList.append(audioData[i])
                counter = 0
        for j in range(twoNum):
            counter2 = counter2 + 1
            if(int(binaryList[j]) % 2 == 0): 
                counter2 = 0
                condensedList.append(0)
            else:
                counter2 = 0
                condensedList.append(1)
            if(len(condensedList) == 7):
                condensedList2.append(condensedList)
                condensedList = []
        self.helper(condensedList2)
        return

    def helper(self,condensedList2):

        list1 = []
        list2 = []
        list3 = []
        for i in range(0, len(condensedList2)):
            num = self.binary_to_decimal(condensedList2[i])
            a = string.printable[num]
            self.secret.append(a)

    def readIn(self,code):
 
        s = Scanner(code)
        rraudio = s.readtoken()
        samplerate = s.readtoken()
        samplerateNum = s.readtoken()
        bits = s.readtoken()
        self.bitsNum = s.readtoken()
        samples = s.readtoken()
        samplesNum = s.readtoken()
        modified = s.readtoken()
        modifiedBy = s.readtoken()
        doubleAmp = s.readtoken()
        self.magicNum = s.readint()
        self.twoNum = s.readint()
        data = s.readint()
        self.audioData = []
        while(data != ""):
            self.audioData.append(data)
            data = s.readint()
        binaryList = self.decodeEngine(self.magicNum, self.audioData, self.twoNum)
        s.close()
        return 
  
    
    def binary_to_decimal(self,binary_digits):
        self.dec_val = int(binary_digits[0])*64
        self.dec_val += int(binary_digits[1])*32
        self.dec_val += int(binary_digits[2])*16
        self.dec_val += int(binary_digits[3])*8
        self.dec_val += int(binary_digits[4])*4
        self.dec_val += int(binary_digits[5])*2
        self.dec_val += int(binary_digits[6])*1
        return self.dec_val

def main():
    
    d = Decode()
    d.decoder()
    d.__str__()
main()
