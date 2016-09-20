Diceware Class
==============
A python class for generating diceware passphrases (with white spaces).

Usage
------
You have to import the class from another Python Script. The object has a method to generate the passphrases with 3 parameters: size, dictionary and secure.
Example available (*example.py*).
The file '*dicts.db*' contains all words of both dictionaries to use in passphrases generation process, it's a *sqlite3* database. 

Parameters
----------
* **size**: This parameter specifies the amount of words to generate.
* **dictionary**: Can be '*diceware*' (standard) or '*beale*' (optional). Default is *diceware*.
* **secure**: Can be 'True' or 'False' (boolean). This add a special character from a table on a random character from a random word of generated passphrase.

About Passphrase Size
---------------------
* Choose 5 words for normal password.
* Choose 6 words for GPG, WiFi or File encryption.
* Choose 7-8 words for high security (BitCoin or another).

More info about diceware [here](http://world.std.com/~reinhold/diceware.html).

