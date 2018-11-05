# import random module
import random
# import time module
import time
# import plotting tools
import matplotlib.pyplot as plt

# Declaring Time Multiplier Constant
TIME_MULTIPLIER = 1000

# Declaring test data related constants
NUMBER_OF_DATAS = 10000
NUMBER_OF_TESTS = 10

# Creating a dataset and filling it with random integers
dataset = []
for i in range(NUMBER_OF_DATAS):
    dataset.append(random.randint(0, 10000))


# Function to do Insertion Sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merges two sub-arrays of arr[].
# First sub-array is arr[l..m]
# Second sub-array is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a Max-Heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Function to do standard partitioning
# This function takes last element as pivot
# The pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

# Function to do randomized partitioning
def randomizedPartition(arr, low, high):
    # Pick a random pivot
    randomPivot = random.randint(low, high)

    # Swap it with the normal pivot
    arr[high], arr[randomPivot] = arr[randomPivot], arr[high]

    return partition(arr, low, high)

# The main function that implements Quick Sort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = randomizedPartition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

###               <-- Timing -->               ###

# Declaring an array for keeping the number
# of integers to put in X-Axis of the plot
numberOfDatas = []

# Declaring some arrays for keeping the
# times to put in Y-Axis of the plot
insertionSortTimes = []
mergeSortTimes = []
heapSortTimes = []
quickSortTimes = []

# Declaring an array to use as the temporary dataset
testData = []

# Looping through different sizes of data
for i in range(NUMBER_OF_TESTS):
    # Putting different data sizes into a list
    numberOfDatas.append((i + 1) * (NUMBER_OF_DATAS // NUMBER_OF_TESTS))

    # Clearing the temporary dataset
    testData.clear()

    # Filling the temporary dataset
    for j in range(numberOfDatas[i]):
        testData.append(dataset[j])

    # Insertion Sort start time
    startTime = time.time()

    # Doing the Insertion Sort
    insertionSort(testData)

    # Insertion Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    insertionSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)

    # Clearing the temporary dataset
    testData.clear()

    # Filling the temporary dataset
    for j in range(numberOfDatas[i]):
        testData.append(dataset[j])

    # Merge Sort start time
    startTime = time.time()

    # Doing the Merge Sort
    mergeSort(testData, 0, numberOfDatas[i] - 1)

    # Merge Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    mergeSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)

    # Clearing the temporary dataset
    testData.clear()

    # Filling the temporary dataset
    for j in range(numberOfDatas[i]):
        testData.append(dataset[j])

    # Heap Sort start time
    startTime = time.time()

    # Doing the Heap Sort
    heapSort(testData)

    # Heap Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    heapSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)

    # Clearing the temporary dataset
    testData.clear()

    # Filling the temporary dataset
    for j in range(numberOfDatas[i]):
        testData.append(dataset[j])

    # Quick Sort end time
    startTime = time.time()

    # Doing the Quick Sort
    quickSort(testData, 0, numberOfDatas[i] - 1)

    # Quick Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    quickSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)


###               <-- Plotting -->               ###

# Plotting the Insertion Sort
plt.plot(numberOfDatas, insertionSortTimes, label="Insertion Sort")
# Plotting the Merge Sort
plt.plot(numberOfDatas, mergeSortTimes, label="Merge Sort")
# Plotting the Heap Sort
plt.plot(numberOfDatas, heapSortTimes, label="Heap Sort")
# Plotting the Quick Sort
plt.plot(numberOfDatas, quickSortTimes, label="Quick Sort")

# Naming the Axises
# Naming the X-Axis
plt.xlabel("Number of Integers")
# Naming the Y-Axis
plt.ylabel("Elapsed time (Milliseconds)")

# Setting a title for the graph
plt.title("Non-Linear Sort Algorithms Comparison")

# Showing a legend on the graph
plt.legend()

# Function to show the graph
plt.show()