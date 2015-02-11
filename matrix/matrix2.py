import sys
import random

# This creates a matrix looking effect with all numbers
def main():
    lines = sys.argv[1]
    printer(int(lines))
    return

def printer(lines):

    for i in range(lines):
        randline = ""
        for x in range(0, 100):
            rand = random.randint(0,9)
            randline = str(rand) + randline
        print(randline)
    return
            

main()
