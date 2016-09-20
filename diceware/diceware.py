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

import random,sqlite3

class dice:
    def __init__(self,size=5,dictionary="diceware",secure=True):
        self.DATABASE="diceware/dicts.db" 
        self.words=[]
        self.dictionary=dictionary
        self.size=size
        self.extra_secure=secure

    def generate(self):
        con=sqlite3.connect(self.DATABASE)
        cur=con.cursor()
        while self.size>0:
            key=""
            i=0
            while i<5:
                key = key + "%i" %random.randint(1,6)
                i+=1
            query='SELECT value FROM '+self.dictionary+' WHERE id='+key
            for fila in cur.execute(query):
                self.words.append(fila[0])
            self.size-=1
        cur.close()
        if self.extra_secure==True:
            self.optional_security()
        phrase=""
        for element in self.words:
            phrase=phrase + " " + element
        phrase=phrase.strip()
        return phrase

    def optional_security(self):
        roll_table=[
             ["~","!","#","$","%","^"],
             ["&","*","(",")","-","="],
             ["+","[","]","\\","{","}"],
             [":",";","\"","'","<",">"],
             ["?","/","0","1","2","3"],
             ["4","5","6","7","8","9"]
          ]
        roll=[]	# 0 word select, 1 character, 2 & 3 table coords.
        roll.append(random.randint(0,len(self.words)-1))          # Word
        roll.append(random.randint(0,len(self.words[roll[0]])-1)) # Character
        roll.append(random.randint(0,5))                          # 1st Coord
        roll.append(random.randint(0,5))                          # 2nd Coord
        word=self.words[roll[0]]
        word=list(word)
        word[roll[1]]=roll_table[roll[2]][roll[3]]    # Character selection & replace
        word="".join(word)
        self.words[roll[0]]=word

