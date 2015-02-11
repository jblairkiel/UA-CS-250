#--------------------------- # Combolock Class # Written by Blair Kiel 6/9/14 # make sure to use the TestDriver # in order to open the lock #--------------------------- class Combolock():

def __init__(self):

        self.secret1 = 20
        self.secret2 = 15
        self.secret3 = 25
        self.dial = 0
        return
        
    def Open(self, num1, num2, num3):
        num1 = int(num1 % 40)
        num2 = int(num2 % 40)
        num3 = int(num3 % 40)

        if(abs(num1) == self.secret1):
            if(abs(num2) == self.secret2):
                if(abs(num3) == self.secret3):
                    print("The Lock Opens")
                else:
                    print("(2/3) The Combination is not correct:")
            else:
                print("(1/3) The Combination is not correct:")
                
        else:
            print("(0/3) The Combination is not correct:")
            
    def reset(self):

        self.dial = 0
        return

    def turnLeft(self, ticks):
        for i in range(0, int(ticks)):
            self.dial = self.dial + 1
            print(self.dial % 40)
        return self.dial

    def turnRight(self, ticks):
        for i in range(0, int(ticks)):
            self.dial = self.dial -1
            print(self.dial % 40)
        return self.dial



    

