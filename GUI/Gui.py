import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import tkinter as tk
from tkinterweb import HtmlFrame #import the HTML browser


class Gui:
    def __init__(self):
        root = tk.Tk() #create the tkinter window

        
    def print_map(self, map):
        root = tk.Tk() #create the tkinter window
        frame = HtmlFrame(root) #create HTML browser

        frame.load_html(map) #load a website
        frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
        root.mainloop()