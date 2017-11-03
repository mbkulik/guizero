from tkinter import Entry, StringVar, END
from . import utilities as utils

class TextBox:

    def __init__(self, master, text="", width=10, grid=None, align=None):

        # Description of this object (for friendly error messages)
        self.description = "[TextBox] object with text \"" + str(text) + "\""

        # Set up controlling string variable
        self._text = StringVar()
        self._text.set( str(text) )

        # Create a tk Label object within this object
        self.tk = Entry(master, textvariable=self._text, width=width)

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)


    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        return self._text.get()

    @value.setter
    def value(self, value):
        self._text.set( str(value) )
        self.description = "[Text] object with text \"" + str(value) + "\""


    # METHODS
    # -------------------------------------------
    # Clear text box
    def clear(self):
        self.tk.delete(0, END)

    # Append text
    def append(self, text):
        self.value = self.value + str(text) 
        self.description = "[Text] object with text \"" + self.value + "\""


    # DEPRECATED METHODS
    # --------------------------------------------
    # Returns the text
    def get(self):
        return self._text.get()

    # Sets the text
    def set(self, text):
        self._text.set( str(text) )
        self.description = "[Text] object with text \"" + str(text) + "\""
