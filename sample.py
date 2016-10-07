#! /usr/bin/env python

# Copyright (C) 2015 Jordi Castello <jordic90@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

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

