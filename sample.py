#! /usr/bin/env python

# Example: dice = diceware.dice(size=2, dictionary="beale", secure=False)
# Or:      dice = diceware.dice(size=10, secure=True)
# Or:      dice = diceware.dice()
#
# And method call: passphrase = dice.generate()

from diceware import diceware

print ""
print "PyDice Example:"
print "---------------"
size = input("Enter the size of passphrasse (amount of words): ")

dice = diceware.Dice(size, dictionary="diceware", secure=True)

print dice.generate()

