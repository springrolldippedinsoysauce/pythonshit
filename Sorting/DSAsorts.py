#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import math


def bubbleSort(A):
    passnum = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True  # Assume is_sorted - we'll find out if it's not
        for ii in range(0, len(A) - passnum - 1):  # NOTE: 0-based array indexing
            if A[ii] > A[ii + 1]:
                temp = A[ii]  # Swap out-of-order elements ii and ii+1
                A[ii] = A[ii + 1]
                A[ii + 1] = temp
                is_sorted = False  # Still need to continue sorting
        passnum += 1  # Next pass


# bubbleSort()

def insertionSort(A):
    for nn in range(len(A) - 1):
        min_idx = nn
        for jj in range(nn + 1, len(A) - 1):
            if A[jj] < A[min_idx]:
                min_idx = jj
        temp = A[min_idx]
        A[min_idx] = A[nn]
        A[nn] = temp


# insertionSort()

def selectionSort(A):
    for nn in range(1, len(A) - 1):
        ii = nn
        while ii > 0 and A[ii - 1] > A[ii]:
            temp = A[ii]
            A[ii] = A[ii - 1]
            A[ii - 1] = temp
            ii -= 1


# selectionSort()

def merge(A, leftIdx, midIdx, rightIdx):
    i = leftIdx
    j = midIdx + 1
    temp = []

    while i <= midIdx and j <= rightIdx:
        if A[i] <= A[j]:
            temp.append(A[i])
            i = i + 1
        else:
            temp.append(A[j])
            j = j + 1

    while i <= midIdx:
        temp.append(A[i])
        i = i + 1

    while j <= rightIdx:
        temp.append(A[j])
        j = j + 1

    index = leftIdx
    for e in temp:
        A[index] = e
        index = index + 1


def mergeSortRecurse(A, leftIdx, rightIdx):
    if (leftIdx < rightIdx):
        midIdx = math.floor((leftIdx + rightIdx) / 2)
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)


def mergeSort(A):
    mergeSortRecurse(A, 0, len(A) - 1)


def quickSort(A):
    if len(A) > 1:
        pivotIdx = int(len(A) / 2)
        pivot = A[pivotIdx]
        A[pivotIdx] = A[-1]
        A[-1] = pivot

        curIdx = 0
        for i in range(0, len(A) - 1):
            if A[i] < pivot:
                temp = A[i]
                A[i] = A[curIdx]
                A[curIdx] = temp
                curIdx = curIdx + 1

        A[-1] = A[curIdx]
        A[curIdx] = pivot
        quickSort(A[:curIdx])
        quickSort(A[curIdx + 1:])
# quickSort()
