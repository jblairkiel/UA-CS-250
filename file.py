# A Class for addresses



class Address():

    def __init__(self, houseN, street, city, zipCode, state = "Alabama", aptNum = None ):
        self.houseNum = houseN
        self.street = street
        self.aptNum = aptNum
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def __str__(self):
        s = str(self.houseNum)+ ' ' + self.street + '\n'
        s += self.city + ' ' + self.state + ' ' + self.zipCode + '\n'
        #print("Type of s:", type(s))
        return s

#    def print(self):
#        print(self.houseNum, self.street)
#        print(self.city, self.state, self.zipCode)

    def __lt__(self, other):
        return self.zipCode < other.zipCode

    def comesBefore(self, other):
        return self.zipCode < other.zipCode

    def comesAfter(self, other):
        return other < self

# Driver test program to test Address.

addr = Address(42, '15th', 'Tuscaloosa', '35404',"Alabama")
print(addr)

addr2 = Address(543, "18th Street", "Tuscaloosa", "35405")
print(addr2)

print(addr.comesBefore(addr2) )
print('This should be True.')
print(addr2.comesBefore(addr) )
print("This should be False.")

print(addr.comesAfter(addr2) )
print('This should be False. ') 
print(addr2.comesAfter(addr) )
print("This should be True. ")

if self == other:
    print("Suprise!!")
    
