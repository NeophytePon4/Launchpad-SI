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

    def turnOnXY(self, lightXY, color=36):
        self.output.note_on(note=self.COORDS_SESSION[lightXY[0]][lightXY[1]], velocity=color, channel=0)

    def turnOffXY(self, lightXY):
        self.output.note_off(note=self.COORDS_SESSION[lightXY[0]][lightXY[1]], channel=0)

    def multiOffXY(self, lightXY):
        for i in range(len(lightXY)):
            self.output.note_off(note=self.COORDS_SESSION[lightXY[i][0]][lightXY[i][1]], channel=0)

    def reset(self):
        for i in range(max(max(self.COORDS_SESSION))):
            self.output.note_off(note=i, channel=0)

    def printLetter(self, letter, color=36, time=1):
        letter = self.getLetter("A")
        for i in range(len(letter)):
            self.turnOnXY(letter[i], color)
        self.multiOffXY(letter)
    
    def scrollWord(self, letter, color=36, time=0):
        pass

    @staticmethod
    def getLetter(image):
        images = json.load(open("Chars.json"))
        letter = images["letters"]
        return letter[image]

    @staticmethod
    def getWord(image):
        pass

if __name__ == "__main__":
    lp = LaunchpadMK2(1, 3)

    #lp.printLetter("A")
    print(len(lp.getLetter("A")))
    lp.scrollWord("H")
    sleep(2)
    lp.reset()
    midi.quit()