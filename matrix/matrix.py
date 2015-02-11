import sys
import random

# This creates a matrix-like effect with 1's and 0's

def main():
    lines = sys.argv[1]
    printer(int(lines))
    return

def printer(lines):

    for i in range(lines):
        randline = ""
        for x in range(0, 100):
            rand = random.randint(0,1)
            randline = str(rand) + randline
        print(randline)
    return
            

main()
