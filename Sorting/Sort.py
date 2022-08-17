import time
import Auxiliary.Auxiliary as Auxiliary
######################## Bubble Sort ##############################
def bubbleSort(rects):
    for i in range(len(rects)):
        # Artifical Delay...
        time.sleep(Auxiliary.TIMEDELAY)
        for j in range(i+1,len(rects)):
            rects[j].setColor('red')
            # Artifical Delay...
            time.sleep(Auxiliary.TIMEDELAY)
                
            if (rects[j].height < rects[i].height):
                Auxiliary.swap(rects, i, j)
                rects[i].setColor('red')

            rects[j].setColor('white')
        rects[i].setColor('white')
######################## Selection Sort ##############################
def selectionSort(rects):
    for i in range(len(rects)):
        minIndex = i
        # Artifical Delay...
        time.sleep(Auxiliary.TIMEDELAY)
        for j in range(i+1, len(rects)):
            rects[j].setColor('red')
            # Artifical Delay...
            time.sleep(Auxiliary.TIMEDELAY)
            
            if (rects[j].height < rects[minIndex].height):
                minIndex = j
            rects[j].setColor('white')
            rects[minIndex].setColor("orange")
        Auxiliary.swap(rects, i, minIndex)
        rects[i].setColor('white')
######################## Insertion Sort ##############################
def insertionSort(rects):
    for i in range(1,len(rects)):
        # Artifical Delay...
        time.sleep(Auxiliary.TIMEDELAY)
        for j in range(i, 0, -1):
            rects[j].setColor('red')
            # Artifical Delay...
            time.sleep(Auxiliary.TIMEDELAY)

            if (rects[j].height < rects[j-1].height):
                Auxiliary.swap(rects, j, j-1)
            
            rects[j].setColor('white')
######################## Quick Sort ##############################
def quickSort(rects):
    qsort(rects, 0, len(rects)-1)

def qsort(rects, lo, hi):
    if (hi <= lo):
        return
    piv = partition(rects, lo, hi)
    rects[hi].setColor('cyan')
    qsort(rects, lo, piv-1)
    qsort(rects, piv+1, hi)
    rects[hi].setColor('white')

def partition(rects, lo, hi):
    pivot = rects[lo]
    pivot.setColor('orange')

    i = lo
    j = hi + 1

    while True:
        i += 1
        # Artifical Delay...
        time.sleep(Auxiliary.TIMEDELAY)
        while (rects[i].height < pivot.height):
            rects[i].setColor('red')
            time.sleep(Auxiliary.TIMEDELAY)
            if (i == hi):
                rects[i].setColor('white')
                break
            rects[i].setColor('white')
            i += 1
        j -= 1
        while (pivot.height < rects[j].height):
            rects[j].setColor('red')
            time.sleep(Auxiliary.TIMEDELAY)
            if (j == lo):
                rects[i].setColor('white')
                break
            rects[j].setColor('white')
            j -= 1
        if (i >= j):
            break
        Auxiliary.swap(rects, i, j)
    Auxiliary.swap(rects, lo, j)
    pivot.setColor('white')

    return j



######################## Merge Sort ##############################
#def merge(rects, lo, mid, hi):
#    print("merge()")
#    i = lo
#    j = mid+1
#    aux = rects

#    for k in range(lo, hi):
#        aux[k] = rects[k]
    
#    for k in range(lo, hi):
#        time.sleep(Auxiliary.TIMEDELAY)
#        if (i > mid):
#            pos = rects[k].pos
#            rects[k] = aux[j]
#            rects[k].moveX(pos[0])
#            j += 1
#        elif (j > hi):
#            pos = rects[k].pos
#            rects[k] = aux[i]
#            rects[k].moveX(pos[0])
#            i += 1
#        elif (aux[j].height < aux[i].height):
#            pos = rects[k].pos
#            rects[k] = aux[j]
#            rects[k].moveX(pos[0])
#            j += 1
#        else:
#            pos = rects[k].pos
#            rects[k] = aux[i]
#            rects[k].moveX(pos[0])
#            i += 1

#def sort(rects, lo, hi):
#    print("sort()")
#    print("lo: {0}".format(str(lo)))
#    print("hi: {0}".format(str(hi)))
#    if (hi <= lo):
#        return
#    mid = lo + (hi - lo) // 2
#    sort(rects, lo, mid)
#    sort(rects, mid+1, hi)
#    merge(rects, lo, mid, hi)

#def mergeSort(rects):
#    print("mergeSort()")
#    aux = rects
#    sort(rects, 0, len(rects)-1)
#    for rect in rects:
#        print(rect.height)