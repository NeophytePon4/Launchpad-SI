from pygame import midi
import json
from time import sleep
import numpy as np
from pprint import pprint
from random import randint

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
        for i in range(max(max(self.COORDS_SESSION)) +1):
            self.output.note_off(note=i, channel=0)

    def printLetter(self, letter, color=36, time=1):
        if type(letter) == str:
            letter = self.getLetter(letter)
            for i in range(len(letter)):
                self.turnOnXY(letter[i], color)
        else:
            
            for i in range(len(letter)):
                self.turnOnXY(letter[i], color)


        sleep(time)
        #self.multiOffXY(letter)
        #self.reset()
    
    #Be warned! This is the most evil function in programming history...
    def scrollWord(self, letter, color=36, time=0):

        #If the word is a single letter
        if len(letter) < 2:
            letter = self.getLetter(letter)
            for i in range(len(letter)):
                letter[i][1] += 9
            
            for i in range(10):
                
                try:
                    self.printLetter(letter, time=0.1)
                except:
                    pass

                for n in range(len(letter)):
                    letter[n][1] -= 1
            print("A single letter")

        #If the word is more than 1
        #Word
        elif len(letter) > 1:
            

            letter = self.getWord(letter)
            
            
            #This piece of code is the bane of my existence.
            for i in range(len(letter)):
                for n in range(len(letter[i])):
                    letter[i][n][1] += 9 * i
                    
            with open("Debug.json", "w") as outfile:
                json.dump(d, outfile)
            
            for i in range(10 * len(letter)):

                for n in range(len(letter)):
                    for x in range(len(letter[n])):
                        if letter[n][x][1] >= 0:
                            positive = True
                        else:
                            
                            positive = False
                    if positive:
                        try:
                        
                            self.printLetter(letter[n], time=0.1)
                            
                        except IndexError:
                            pass

                for n in range(len(letter)):
                    for x in range(len(letter[n])):
                        letter[n][x][1] -= 1
                        if letter[n][x][1] < 0:
                            letter[n][x][1] = -100
                        
                self.reset()
                            
    def readButtonPressed(self):
        coord = None
        state = None
        r = self.read.read(1)
        #print("Read value: {}".format(r))
        if len(r) > 0 and r[0][0][2] == 127:
            try:
                for i, subList in enumerate(self.COORDS_SESSION):
                    if r[0][0][1] in subList:
                        place = subList.index(r[0][0][1])

                        coord = [i, place]
                        state = True

            except IndexError as e:
                coord = None

        elif len(r) > 0 and r[0][0][2] == 0:
            try:
                for i, subList in enumerate(self.COORDS_SESSION):
                    if r[0][0][1] in subList:
                        place = subList.index(r[0][0][1])
                        
                        coord = [i, place]
                        state = False
            except IndexError as e:
                coord = None

        else:
            coord = None

        return coord, state

    @staticmethod
    def getLetter(image):
        images = json.load(open("Chars.json"))
        letter = images["letters"]
        return letter[image.upper()]

    @staticmethod
    def getWord(word):
        chars = json.load(open("Chars.json"))
        
        letters = chars["letters"]
        outp = [[] for x in range(len(word))]

        for i in range(len(word)):
            outp[i] = letters[word[i].upper()]
        
        return outp

if __name__ == "__main__":
    print("Starting...")
    lp = LaunchpadMK2(1, 3)
    lp.reset()
    #lp.printLetter("A")
    #lp.scrollWord("Lol") - Never uncomment this. Ever.
    print("Running!")
    
    while True:
        
        s = lp.readButtonPressed()
        if s[0] and s[1] is not None:
            print(s[0])
        
        if s[0] == [7, 8]:
            lp.reset()
            midi.quit()
            quit()
        
        elif s[1]:
            lp.turnOnXY(s[0])
            
        elif s[1] is False:
            lp.turnOffXY(s[0])

    lp.reset()
    midi.quit()