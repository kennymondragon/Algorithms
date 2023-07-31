from Auxiliary.graphics import *
import Auxiliary.Auxiliary as Auxiliary
import Sorting.Sort as Sort
import datetime
import sys


def main(args):
    win = GraphWin("Algorithms", 1200, 700)

    if (args[1] == 'sort'):
        rects = Auxiliary.generateRandomRects(win, int(args[2]), 10, 15, 10, 50, 200)
    
        startTime = datetime.datetime.now()

        if (args[3].lower() == "bubblesort"):
            Sort.bubbleSort(rects)
        if (args[3].lower() == "selectionsort"):
            Sort.selectionSort(rects)
        if (args[3].lower() == "insertionsort"):
            Sort.insertionSort(rects)
        if (args[3].lower() == "quicksort"):
            Sort.quickSort(rects)
        if (args[3].lower() == "mergesort"):
            Sort.mergeSort(rects)

        stopTime = datetime.datetime.now()
        sortTime = Text(Point(100, 250), "Sorted in {0}s".format(stopTime - startTime))
        sortTime.draw(win)
        print(stopTime - startTime)
        Auxiliary.validateSort(rects)
    elif (args[1] == 'struct'):
        root = None
        arr = list(map(lambda num: int(num), args[3].split(',')))
        print(arr)
        if (args[2] == 'btree'):
            Auxiliary.buildBTree(arr, root, win)
    win.getMouse()

main(sys.argv)