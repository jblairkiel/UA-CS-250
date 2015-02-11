
class Card():
    
    def __init__(self, t, value):

        self.typ = t
        self.value = value

    def setName(self, name):
        
        self.name = name

    def __str__(self):
        
        s = self.typ + " " + str(self.value)

class RookCard(Card):

    def __init__(self, t, value, color):
        
        super().__init__(t, value)
        self.color = color

    def __str__(self):
        s = super().__str__()
        s += ' ' + self.color

def main():

    c = RookCard("Rook", 10, "red")
    print(c)
    c.setName("Hello")
    print(c)

main()
