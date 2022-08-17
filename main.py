from Auxiliary.graphics import *
import Auxiliary.Auxiliary as Auxiliary
import Sorting.Sort as Sort
import datetime
import sys


def main(args):
    print(args[1])
    win = GraphWin("Algorithms", 1200, 700)
    rects = Auxiliary.generateRandomRects(win, int(args[1]), 10, 15, 10, 50, 200)
    
    startTime = datetime.datetime.now()

    if (args[2].lower() == "bubblesort"):
        Sort.bubbleSort(rects)
    if (args[2].lower() == "slectionsort"):
        Sort.selectionSort(rects)
    if (args[2].lower() == "insertionsort"):
        Sort.insertionSort(rects)
    if (args[2].lower() == "quicksort"):
        Sort.quickSort(rects)

    stopTime = datetime.datetime.now()
    sortTime = Text(Point(100, 250), "Sorted in {0}s".format(stopTime - startTime))
    sortTime.draw(win)
    print(stopTime - startTime)
    Auxiliary.validateSort(rects)
    win.getMouse()

main(sys.argv)