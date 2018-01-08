from pygame import midi
import json
from time import sleep
import numpy as np

class LaunchpadMK2:

    COORDS_SESSION = [
        [81, 82, 83, 84, 85, 86, 87, 88, 89],
        [71, 72, 73, 74, 75, 76, 77, 78, 79],
        [61, 62, 63, 64, 65, 66, 67, 68, 69],
        [51, 52, 53, 54, 55, 56, 57, 58, 59],
        [41, 42, 43, 44, 45, 46, 47, 48, 49],
        [31, 32, 33, 34, 35, 36, 37, 38, 39],
        [21, 22, 23, 24, 25, 26, 27, 28, 29],
        [11, 12, 13, 14, 15, 16, 17, 18, 19]
        ]
    
    def __init__(self, readChennel, outputChannel):
        midi.init()
        self.read = midi.Input(readChennel)
        self.output = midi.Output(outputChannel)

    def turnOnXY(self, lightXY, color):
        self.output.note_on(note=self.COORDS_SESSION[lightXY[1]][lightXY[0]], velocity=color, channel=0)


if __name__ == "__main__":
    lp = LaunchpadMK2(1, 3)
    lp.turnOnXY([0, 1], 44)