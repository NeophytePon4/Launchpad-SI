print("Loading...")
import cv2
import numpy as np
import json


class FastFrame():
    """
    Types:
    -img
    -ani
    -seq
    Styles:
    -bw (black and white)
    -gr (grey style)
    -fc (Full colour)
    """

    def __init__(self, img, name, type):
        print("Done!")
        self.type = type
        self.style = "bw"
        self.export = "Animations.json"
        self.name = name
        self.arr = {self.name : []}
        if self.type == "img":
            self.img = cv2.imread(img)
        elif self.type == "seq":
            self.img = cv2.VideoCapture(img)

    def decode(self):
        if self.type == "img" and self.style == "bw":

            #Whenever it finds black
            for i in range(len(self.img)):
                for n in range(len(self.img[i])):
                    if np.any(self.img[i][n]) == np.all([0,0,0]):
                        self.arr[self.name].append([i, n])

                    elif np.any(self.img[i][n]) == np.all([255,255,255]):
                        print("White")

                    else:
                        print("Fail - " + str(self.img[i][n]))

        elif self.type == "seq" and self.style == "bw":
            #rect, self.gif = self.img.read()
            #print("Image data: {}".format(self.gif))
            i = 0
            rect = True
            gif = []

            while rect == True:
                rd = self.img.read()
                
                rect = rd[0]
                gif.append(rd[1])
                i += 1
            
            #for i in range(len(self.img)):
            #    for n in range(len(self.img[i])):
            #        if np.any(self.img[i][n)

        print(self.arr)

    def writeToJson(self):
        if self.type == "img":
            try:
                before = json.load(open("Animations.json"))
            except:
                before = None

            with open(self.export, "w", encoding="utf-8") as dataFile:
                if before != None:
                    #json.dump(before.setdefault(self.arr), dataFile)
                    print(list(self.arr.keys()))
                    before[list(self.arr.keys())[0]] = self.arr[list(self.arr.keys())[0]]
                    json.dump(before, dataFile)
                else:
                    json.dump(self.arr, dataFile)

exit = False
while exit == False:
    print("Please enter the image path/name")
    img = input(">>")

    print("What do you wish to name the image?")
    name = input(">>")

    print("Img or seq?")
    type = input(">>").lower()

    fastFrame = FastFrame(img, name, type)

    fastFrame.decode()
    fastFrame.writeToJson()

    print("Quit?")
    e = input(">>")
    if e.lower() == "yes" or e.lower() == "y":
        exit = True
    elif e.lower == "no" or e.lower() == "n":
        exit = False
    else:
        print("Not a valid answer")