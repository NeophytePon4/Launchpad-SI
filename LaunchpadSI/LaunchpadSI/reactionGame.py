from pygame import midi
import json
import time
import numpy as np
from pprint import pprint
from LaunchpadSI import LaunchpadMK2
from random import randint

class launchpadGame(LaunchpadMK2):
    pass
    

class reactionGame(launchpadGame):
    COMBO_SPEED = 0.1
    SEGMENTS = 1
    THEME = 43

    def __init__(self, readChennel, outputChannel):
        super().__init__(readChennel, outputChannel)
        self.buttons = [[]]
    
    def display(self, coords):
        for i in range(len(coords)):
            self.turnOnXY(coords[i], color=self.THEME)

    def generateCoord(self):
        if self.SEGMENTS == 1:
            x = str(randint(1, 4))
            y = str(randint(1, 4))
            xy = int(x + y)
            return xy

    def gameLoop(self):
        while exit is not True:
            self.display([[1, 3], [4, 4]])
lp = reactionGame(1, 3)
lp.generateCoord()
lp.gameLoop()