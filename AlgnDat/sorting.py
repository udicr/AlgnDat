import numpy as np
from random import randint

a = 100 * np.random.rand(100)
n = len(a)


def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True


def swap(ar, i, j):
    ar[i], ar[j] = ar[j], ar[i]


def bubble_sort(array):
    swaps = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                swaps += 1
                swapped = True
        if not swapped:
            break
    print(array)
    print(swaps)


def selection_sort(array):
    swaps = 0
    for i in range(len(array)):

        tmp, = np.where(array == min(array[i:]))
        if tmp > i:
            swap(array, i, tmp)
            swaps += 1
    print(array)
    print(swaps)


def insertion_sort(array):
    inserts = 0
    for i in range(1, n):

        tmp = min(np.where(array[:i] >= array[i]))
        if len(tmp) > 0:
            t = tmp[0]
            array = np.delete(np.insert(array, t, array[i]), i + 1)

            inserts += 1
        else:
            pass

    print(array)
    print(inserts)


def merge(la, ra):
    ar = np.array([])
    ln = len(la)
    rn = len(ra)
    l = 0
    r = 0
    for i in range(ln + rn):
        if l >= ln:
            ar = np.concatenate((ar, ra[r:]))
            return ar
        elif r >= rn:
            ar = np.concatenate((ar, la[l:]))
            return ar
        elif la[l] <= ra[r]:
            ar = np.append(ar, la[l])
            l += 1
        else:
            ar = np.append(ar, ra[r])
            r += 1


def merge_sort(array):  # todo: make a version with linked lists for better storage behavior
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def partition(array, start, end):
    done = False
    end -= 1
    pivot = array[-1]
    while not done:

        while array[start] <= pivot and start <= end:
            start += 1

        while array[end] >= pivot and end >= start:
            end -= 1
        if end < start:
            done = True
        else:
            swap(array, start, end)
    return end


def rand_quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot = randint(start, end)
        swap(array, end, pivot)
        split = partition(array, start, end)

        rand_quick_sort(array, start, split - 1)
        rand_quick_sort(array, split + 1, end)


rand_quick_sort(a)
print(len(a))
print(is_sorted(a))
