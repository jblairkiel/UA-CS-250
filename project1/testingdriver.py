from p1 import Combolock

#----------------------------------------------------
#   Project 1 "The Combolock" written by Blair Kiel
#
#   TestDriver simulates turning the dial, opening
#   the lock and resetting it.  This assumes the values
#   that are being input, are being turned correctly
#   in the correct order:    right, left
#   then back right. I left print statements on, in
#   order to prove the code works as intended.
#   if you have any questions, please contact me.
#
#----------------------------------------------------

def main():
    
    print("Guess how many times to turn the dial...")
    turn1 = input("First turn: ")
    turn2 = input("Second turn: ")
    turn3 = input("Third turn: ")
    lock = Combolock()

    print("Turning right " + turn1 + " times.")
    num1 = lock.turnRight(turn1)

    print("Turning left " + turn2 + " times.")
    num2 = lock.turnLeft(turn2)

    print("Turning right "+ turn3 + " times.")
    num3 = lock.turnRight(turn3)

    print("Attempting to Open the Lock")
    lock.Open(num1, num2, num3)
    lock.dial = lock.dial % 40
    num1 = num1 % 40
    num2 = num2 % 40
    num3 = num3 % 40

    print("Resetting the Lock")
    lock.reset()
    print("dial = " + str(lock.dial))
    print("Secret #1 = " + str(lock.secret1))
    print("Secret #2 = " + str(lock.secret2))
    print("Secret #3 = " + str(lock.secret3))

main()



