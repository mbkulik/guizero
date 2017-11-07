from tkinter import Canvas, BOTH, Frame
from . import utilities as utils

class Waffle:

    def __init__(self, master, height=3, width=3, dim=20, pad=5, color="white", dotty=False, remember=True, grid=None, align=None, command=None):

    	# Description of this object (for friendly error messages)
        self.description = "[Waffle] object ("+str(height)+"x"+str(width)+")"

        self._command = command
        self._height = height       # How many pixels high
        self._width = width         # How many pixels wide
        self._pixel_size = dim      # Size of one pixel
        self._pad = pad             # How much padding between pixels
        self._color = color        # Start color of the whole waffle
        self._dotty = dotty         # A dotty waffle will display circles
        self._save_colors = []

        # Set up a pixel array to remember the pixel colours if remember was True
        self._save_colors = [[color for row in range(self._width)] for col in range(self._height)]

        # Calculate how big this canvas will be
        self._c_height = self._width*(self._pixel_size+self._pad)
        self._c_width = self._width*(self._pixel_size+self._pad)

        # Create a tk Frame object within this object which will be the waffle
        self.tk = Frame(master.tk)

        # Create an internal canvas to draw the waffle on
        self._canvas = Canvas(self.tk, height=self._c_height, width=self._c_width)

        # Draw the pixels on the canvas
        self._draw(self._color)

        # Pack the canvas into this Waffle object
        self._canvas.pack(fill=BOTH, expand=1)

        # Bind the left mouse click to the canvas so we can click on the waffle
        self._canvas.bind("<Button-1>", self._clicked_on)

        # Pack this box into its layout
        utils.auto_pack(self, master, grid, align)

    # METHODS
    # -------------------------------------------

    # Internal use only
    def _draw(self, color):
        # Draw the pixels on the canvas
        currx = self._pad
        curry = self._pad

        for y in range(self._height):
            for x in range(self._width):
                if self._dotty == False:
                    self._canvas.create_rectangle(currx, curry, currx+self._pixel_size, curry+self._pixel_size, fill=color)
                else:
                    self._canvas.create_oval(currx, curry, currx+self._pixel_size, curry+self._pixel_size, fill=color)
                currx = currx + self._pixel_size + self._pad
            curry = curry + self._pixel_size + self._pad
            currx = self._pad

    # Sets the colour of the whole waffle
    def set_all(self, color):
        self._color = str(color)
        self._draw(self._color)
        self._save_colors = [[self._color for row in range(self._width)] for col in range(self._height)]

    # Sets a single pixel
    def set_pixel(self, x, y, color):
        if x >= self._width:
            utils.error_format("The x value "+ str(x) + " is off the edge of the waffle")
        elif y >= self._width:
            utils.error_format("The y value "+ str(y) + " is off the edge of the waffle")
        else:
            locate_x = (self._pixel_size + self._pad) * int(x) + self._pad
            locate_y = (self._pixel_size + self._pad) * int(y) + self._pad
            if self._dotty == False:
                self._canvas.create_rectangle(locate_x, locate_y, locate_x+self._pixel_size, locate_y+self._pixel_size, fill=color)
            else:
                self._canvas.create_oval(locate_x, locate_y, locate_x+self._pixel_size, locate_y+self._pixel_size, fill=color)

            # Update the saved colours
            self._save_colors[y][x] = color

    # Returns the colour value of a pixel if set
    def get_pixel(self, x, y):
        return self._save_colors[y][x]

    # Returns a 2D list of all colours in the waffle
    def get_all(self):
        return self._save_colors

    # Internal use only
    # Detect x,y coords of where the user clicked
    def _clicked_on(self,e):
        canvas = e.widget
        x = canvas.canvasx(e.x)
        y = canvas.canvasy(e.y)
        pixel_x = int(x/(self._pixel_size+self._pad))
        pixel_y = int(y/(self._pixel_size+self._pad))
        if self._command:
            self._command(pixel_x,pixel_y)
