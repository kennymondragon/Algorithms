import time
import copy
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
# def merge(rects, lo, mid, hi, aux):
#     print("merge()")
#     i = lo
#     j = mid+1

#     #for k in range(lo, hi):
#     #    aux[k] = rects[k]
#     aux[lo:hi] = rects[lo:hi].copy()

#     for k in range(lo, hi):
#         time.sleep(Auxiliary.TIMEDELAY+1)
#         if (i > mid):
#             pos = rects[k].pos
#             rects[k] = aux[j]
#             rects[k].moveX(pos[0])
#             j += 1
#         elif (j > hi):
#             pos = rects[k].pos
#             rects[k] = aux[i]
#             rects[k].moveX(pos[0])
#             i += 1
#         elif (aux[j].height < aux[i].height):
#             pos = rects[k].pos
#             rects[k] = aux[j]
#             rects[k].moveX(pos[0])
#             j += 1
#         else:
#             pos = rects[k].pos
#             rects[k] = aux[i]
#             rects[k].moveX(pos[0])
#             i += 1

# def sort(rects, lo, hi, aux):
#     print("sort()")
#     print("lo: {0}".format(str(lo)))
#     print("hi: {0}".format(str(hi)))
#     if (hi <= lo):
#         return
#     mid = lo + (hi - lo) // 2
#     sort(rects, lo, mid, aux)
#     sort(rects, mid+1, hi, aux)
#     merge(rects, lo, mid, hi, aux)

# def mergeSort(rects):
#     print("mergeSort()")
#     aux = (rects.copy())
#     sort(rects, 0, len(rects)-1, aux)
#     for rect in rects:
#         print(rect.height)

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid].copy()
 
        # into 2 halves
        R = arr[mid:].copy()
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].height <= R[j].height:
                arr[k].setColor('cyan')
                time.sleep(Auxiliary.TIMEDELAY+1)
                pos = arr[k].pos
                arr[k] = L[i]
                arr[k].moveX(pos[0])
                i += 1
            else:
                arr[k].setColor('cyan')
                time.sleep(Auxiliary.TIMEDELAY+1)
                pos = arr[k].pos
                arr[k] = R[j]
                arr[k].moveX(pos[0])
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k].setColor('cyan')
            time.sleep(Auxiliary.TIMEDELAY+1)
            pos = arr[k].pos
            arr[k] = L[i]
            arr[k].moveX(pos[0])
            i += 1
            k += 1
 
        while j < len(R):
            arr[k].setColor('cyan')
            time.sleep(Auxiliary.TIMEDELAY+1)
            pos = arr[k].pos
            arr[k] = R[j]
            arr[k].moveX(pos[0])
            j += 1
            k += 1