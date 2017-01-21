import random
import sqlite3


class Dice:
    def __init__(self, size=5, dictionary="diceware", secure=True):
        self.DATABASE = "diceware/dicts.db"
        self.words = []
        self.dictionary = dictionary
        self.size = size
        self.extra_secure = secure

    def generate(self):
        con = sqlite3.connect(self.DATABASE)
        cur = con.cursor()
        while self.size > 0:
            key = ""
            i = 0
            while i < 5:
                key += "%i" % random.randint(1, 6)
                i += 1
            query = 'SELECT value FROM ' + self.dictionary + ' WHERE id=' + key
            for row in cur.execute(query):
                self.words.append(row[0])
            self.size -= 1
        cur.close()
        if self.extra_secure:
            self.optional_security()
        phrase = ""
        for element in self.words:
            phrase = phrase + " " + element
        phrase = phrase.strip()
        return phrase

    def optional_security(self):
        roll_table = [
             ["~", "!", "#", "$", "%", "^"],
             ["&", "*", "(", ")", "-", "="],
             ["+", "[", "]", "\\", "{", "}"],
             [":", ";", "\"", "'", "<", ">"],
             ["?", "/", "0", "1", "2", "3"],
             ["4", "5", "6", "7", "8", "9"]
          ]
        roll = []	# 0 word select, 1 character, 2 & 3 table coords.
        roll.append(random.randint(0, len(self.words)-1))          # Word
        roll.append(random.randint(0, len(self.words[roll[0]])-1)) # Character
        roll.append(random.randint(0, 5))                          # 1st Coord
        roll.append(random.randint(0, 5))                          # 2nd Coord
        word = self.words[roll[0]]
        word = list(word)
        word[roll[1]] = roll_table[roll[2]][roll[3]]    # Character selection & replace
        word = "".join(word)
        self.words[roll[0]] = word

