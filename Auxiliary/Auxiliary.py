from Auxiliary.graphics import *
import random
import time

TIMEDELAY = 0.015

# Rectangle Class
class Rect:
    def __init__(self, pos, width, height) -> None:
        self.pos = pos
        self.width = width
        self.height = height
        self.tl = Point(self.pos[0], self.pos[1])
        self.br = Point(self.pos[0]+self.width, self.pos[1]+(self.height))
        self.rectangle = Rectangle(self.tl, self.br)
    
    def setColor(self, color) -> None:
        self.rectangle.setFill(color)
    
    def draw(self, win) -> None:
        self.win = win
        self.rectangle.draw(win)

    def moveX(self, x) -> None:
        tmp = self.pos[0]
        self.pos[0] = x
        self.rectangle.move(self.pos[0]-tmp, 0)

# Auxiliary Functions
def swap(rectList, rectAIndex, rectBIndex) -> None:
    #Swap rectangles in array
    tmpRect = rectList[rectAIndex]
    rectList[rectAIndex] = rectList[rectBIndex]
    rectList[rectBIndex] = tmpRect

    #Swap rectangles on screen
    tmpRect = rectList[rectAIndex].pos[0]
    rectList[rectAIndex].moveX(rectList[rectBIndex].pos[0])
    rectList[rectBIndex].moveX(tmpRect)

def generateRandomRects(win, numofrects, xoffset, yoffset, width, minheight, maxheight):
    rectangles = []
    for i in range(numofrects):
        rectHeight = random.randrange(minheight,maxheight)
        rect = Rect([xoffset+(width*(i+1)),yoffset+(maxheight-rectHeight)], width, rectHeight)
        rectangles.append(rect)

    for rect in rectangles:
        rect.draw(win)

    return rectangles

def validateSort(rects):
    for i in range(len(rects)-1):
        if rects[i].height > rects[i+1].height:
            return False
        else:
            rects[i].setColor('green')
        time.sleep(TIMEDELAY)
    rects[i+1].setColor('green')
    return True