def swap(a,b,list):
    list[a] = list[a] + list[b]
    list[b] = list[a] - list[b]
    list[a] = list[a] - list[b]

def pull_right(a,b,list):
    for i in range(a,b,-1):
        list[i]=list[i-1]


def SelectionSort1(list):
    k = len(list)
    for i in range(k):
        min_el = list[i]
        p = i
        for j in range(i,k):
            if list[j] < min_el:
                min_el = list[j]
                p = j
        if p==i:
            continue
        swap(p,i,list)


    return list


def SelectionSort(list):
    k = len(list)
    j=0
    while True:
        p = j
        min_el = list[j]
        for i in range(j,k):
            if list[i] < min_el:
                min_el = list[i]
                p = i
        if p!=j:
            swap(j,p,list)
        j+=1
        if j == k-1:
            break
    return(list)


def InsertionSort(list):
    k = len(list)
    for i in range(1,k):
        sel = list[i]
        for j in range(i-1,-1,-1):
            if sel >= list[j]:
                pull_right(i,j+1,list)
                list[j+1] = sel
                break
            if j == 0:
                pull_right(i, 0, list)
                list[0] = sel

    return list


def InsertSort(list):
    k = len(list)
    for i in range(1, k):
        sel = list[i]
        for j in range(i-1, -1, -1):
            if sel < list[j]:
                list[j+1] = list[j]
                list[j] = sel
                continue
            if sel >= list[j]:
                break
    return list


def BubbleSort(list):
    k = len(list)
    while True:
        switch = False
        i = 0
        while i+1 < k:
            if list[i] > list[i+1]:
                switch = True
                swap(i,i+1,list)
            i+=1
        if not switch:
            break
        k-=1
    return (list)


def SelectionSort_Reverse(list):
    k = len(list)
    for i in range(k):
        max_el = list[i]
        p = i
        for j in range(i,k):
            if list[j] > max_el:
                max_el = list[j]
                p = j
        if p==i:
            continue
        swap(p,i,list)
    return list


def quicksort_(list):
    if len(list)<=1:
        return list
    else:
        left = []
        right = []
        k = len(list)
        pivot = list[k - 1]
        for i in range(k):
            if list[i] < pivot:
                left.append(list[i])
            else:
                right.append(list[i])
        return quicksort_(left) + [pivot] + quicksort_(right[:-1])


def quicksort_reverse(list):
    if len(list) <= 1:
        return list
    else:
        left = []
        right = []
        k = len(list)
        pivot = list[k - 1]
        for i in range(k):
            if list[i] > pivot:
                left.append(list[i])
            else:
                right.append(list[i])
        return quicksort_(left) + [pivot] + quicksort_(right[:-1])


# Python program for implementation of MergeSort


def mergesort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


