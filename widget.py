# import tkinter as tk
# from tkniter import *

class widget:

    def __init__(self, frameName):
        self.frameName=frameName

    def button(self):
        return Button(master=self.frameName).pack()

    def label(self):
        return Label(master=self.frameName).pack()

    def frame(self):
        return Frame(master=self.frameName).pack()