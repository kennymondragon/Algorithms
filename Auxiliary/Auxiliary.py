from turtle import pos
from Auxiliary.graphics import *
import random
import time

TIMEDELAY = 0.015
BRANCHDECAY = 1.7

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

# Node Class
class bNode:
    def __init__(self, pos, rad, val, offset=10, left=None, right=None) -> None:
        self.rawPos = pos
        self.pos = Point(pos[0], pos[1])
        self.radius = rad
        self.value = val
        self.left = left
        self.right = right
        self.circle = Circle(self.pos, self.radius)
        self.nodeText = Text(self.pos, str(self.value))
        self.offset = offset
        self.line = None
        self.linept1 = None
        self.linept2 = None

    def draw(self, win) -> None:
        self.win = win
        self.circle.draw(win)
        self.nodeText.draw(win)
    
    def moveX(self, x) -> None:
        tmp = self.rawPos[0]
        self.rawPos[0] = x
        self.pos = Point(self.rawPos[0], self.rawPos[1])
        self.circle.move(self.rawPos[0]-tmp, 0)
        self.nodeText.move(self.rawPos[0]-tmp, 0)
        if self.line != None:
            self.line.move(-10000000, -10000000)
            self.line = Line(self.linept1, Point(self.pos.x, self.linept2.y))
            self.line.draw(self.win)

    def addChild(self, side, val):
        if side == 'left':
            self.left = bNode([self.pos.x-(self.radius*self.offset), self.pos.y+(self.radius*2.5)], self.radius, val, self.offset/BRANCHDECAY)
            self.left.draw(self.win)
            
            pt1 = Point(self.pos.x, self.pos.y+self.radius)
            pt2 = Point(self.pos.x-(self.radius*self.offset), self.pos.y+(self.radius*1.5))
            
            self.left.line = Line(pt1, pt2)
            self.left.linept1 = pt1
            self.left.linept2 = pt2
            self.left.line.draw(self.win)

        if side == 'right':
            self.right = bNode([self.pos.x+(self.radius*self.offset), self.pos.y+(self.radius*2.5)], self.radius, val, self.offset/BRANCHDECAY)
            self.right.draw(self.win)
            pt1 = Point(self.pos.x, self.pos.y+self.radius)
            pt2 = Point(self.pos.x+(self.radius*self.offset), self.pos.y+(self.radius*1.5))
            self.right.line = Line(pt1, pt2)
            self.right.linept1 = pt1
            self.right.linept2 = pt2
            self.right.line.draw(self.win)

def buildBTree(arr, root, win):
    for i in range(len(arr)):
        if root == None:
            root = bNode([win.getWidth()/2, 100], 25, arr[i], len(arr))
            root.draw(win)
        else:
            insertNode(arr[i], root, win)

def insertNode(num, root, win):
    if root.value > num:
        if root.left != None:
            insertNode(num, root.left, win)
        else:
            root.addChild("left", num)
            return
    else:
        if root.right != None:
            insertNode(num, root.right, win)
        else:
            root.addChild("right", num)
            return

#class gNode:
#    def __init__(self, posm rad, value, children=None) -> None:
#        self.rawPos = pos
#        self.pos = Point(pos[0], pos[1])

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