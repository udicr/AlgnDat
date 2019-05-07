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
    i = (start - 1)
    pivot = array[end]
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)

    swap(array, i + 1, end)
    return (i + 1)


def rand_quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot = randint(start, end)
        swap(array, end, pivot)
        split = partition(array, start, end)

        rand_quick_sort(array, start, split - 1)
        rand_quick_sort(array, split + 1, end)


def lin_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1


def bin_search(sorted_array, x, l=0, r=None):
    if r is None:
        r = len(sorted_array)
    if r >= l:
        mid = l + (r - l) // 2
        if sorted_array[mid] == x:
            return mid
        elif sorted_array[mid] > x:
            return bin_search(sorted_array, l, mid - 1, x)
        else:
            return bin_search(sorted_array, mid + 1, r, x)
    else:
        return -1


rand_quick_sort(a)
print(a)
print(is_sorted(a))
print(lin_search(a, 50))
