#! /usr/bin/env python

"""Pydice is a graphical tool that generates passphrases using diceware method."""

__author__ = "Jordi Castello"
__email__  = "jordic90@gmail.com"
__license__= """
    Copyright (C) 2015 Jordi Castello <jordic90@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from Tkinter import *
from diceware import diceware

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(columns=2,rows=7, padx=5, pady=5)
        self.createWidgets()

    def createWidgets(self):
        self.dict_selection=StringVar()
        self.dict_selection.set("diceware")
        self.security_selection=BooleanVar()
        self.security_selection.set(True)

        Label(self, text="Dictionary: ").grid(row=0, column=0, sticky=W)
        self.radio_dict1=Radiobutton(self, text="Diceware", variable=self.dict_selection, value="diceware")
        self.radio_dict2=Radiobutton(self, text="Beale", variable=self.dict_selection, value="beale")
        self.radio_dict1.grid(row=1,column=0, sticky=W)
        self.radio_dict2.grid(row=2,column=0, sticky=W)

        Label(self, text="More Security: ").grid(row=0, column=1, sticky=W)
        self.radio_dict1=Radiobutton(self, text="Yes", variable=self.security_selection, value=True, fg="green")
        self.radio_dict2=Radiobutton(self, text="No", variable=self.security_selection, value=False, fg="red")
        self.radio_dict1.grid(row=1,column=1, sticky=W)
        self.radio_dict2.grid(row=2,column=1, sticky=W)

        Label(self, text="Number of words: ").grid(row=3, column=0, pady=10, sticky=W)
        self.n_words=IntVar()
        self.n_words.set(5)
        self.spin_words=Spinbox(self, from_=1, to=10, textvariable=self.n_words, width=5, background="white")
        self.spin_words.grid(row=3, column=1, sticky=W)

        self.con_boton = Button(self, text="Generate", width=10, command=self.generate)
        self.con_boton.grid(row=4,column=0, sticky=W)

        self.con_boton = Button(self, text="Copy to Clipboard", width=10, command=self.to_clipboard)
        self.con_boton.grid(row=4,column=1, ipadx=5, sticky=W)

        Label(self, text="Result: ").grid(row=5, column=0, pady=5, sticky=W)
        self.texto_salida = Text(self, width=40, height=5, background="white")
        self.texto_salida.grid(row=6, column=0, columnspan=2)

    def generate(self):
        frase=diceware.dice(size=self.n_words.get(), dictionary=self.dict_selection.get(), secure=self.security_selection.get())
        self.texto_salida.delete('1.0',END)
        self.texto_salida.insert(INSERT,frase.generate())

    def to_clipboard(self):
        self.text_value=self.texto_salida.get('1.0',END)
        root.clipboard_clear()
        root.clipboard_append(self.text_value)

    def select_dict(self):
        print str(self.dict_selection.get())

root = Tk()
app = Application(master=root)
app.master.title("Diceware Passgen")

try:    
# To show favicon, if do you have problems, comment out this block
    try:
        app.master.iconbitmap("icons/dice.ico")    # Windows favicon
    except:
        app.master.iconbitmap("@icons/dice.xbm")   # Linux favicon
except:
    print "Can't establish a favicon"

app.master.resizable(0,0)
app.mainloop()
#root.destroy()

