# import mathematical functions module
import math
# import random module
import random
# import time module
import time
# import plotting tools
import matplotlib.pyplot as plt

# Declaring Time Multiplier constant
TIME_MULTIPLIER = 1000

# Declaring test data related constants
NUMBER_OF_DATAS = 100000
NUMBER_OF_TESTS = 100

# Creating a dataset and filling it with random integers
dataset = []
for i in range(NUMBER_OF_DATAS):
    dataset.append(random.randint(100, 999))


# Function to do Counting Sort
def countingSort(array):

    # Maximum index of the counter array
    maxValue = max(array) + 1

    # Initialize a counter array with zeros
    counter = [0] * maxValue

    # Counting the occurences
    for i in array:
        counter[i] += 1

    # Adding up the number of elements
    # that are equal or smaller than i
    for i in range(1, maxValue):
        counter[i] += counter[i - 1]

    # Initializing an output array
    sortedArray = [None] * len(array)

    # Filling the output array considering the order of
    # elements in the input array (doing stable sorting)
    for i in range(len(array) - 1, -1, -1):
        sortedArray[counter[array[i]] - 1] = array[i]
        counter[array[i]] -= 1

    return sortedArray


# Function to do Counting Sort By Digit(to be used in Radix Sort)
def countingSortByDigit(array, radix, exponent, minValue):

    # Create the buckets
    buckets = [0] * radix
    # Create the output array
    sortedArray = [None] * len(array)

    # Count frequencies
    for i in range(0, len(array)):
        bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
        buckets[bucketIndex] += 1

    # Compute cumulates
    for i in range(1, radix):
        buckets[i] += buckets[i - 1]

    # Move the records
    for i in range(len(array) - 1, -1, -1):
        bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
        buckets[bucketIndex] -= 1
        sortedArray[buckets[bucketIndex]] = array[i]

    return sortedArray


def radixSort(array, radix = 10):

    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    # Perform counting sort on each exponent/digit,
    # starting at the least significant digit
    exponent = 1
    while (maxValue - minValue) / exponent >= 1:
        array = countingSortByDigit(array, radix, exponent, minValue)
        exponent *= radix

    return array


# Function to do insertion sort (to be used in Bucket Sort)
def insertionSort(array):

    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):

        key = array[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


def bucketSort(array, bucketSize = 10):

    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    # Initialize the buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])

    # Sort buckets and place back into the given array
    array.clear()

    # Sort the buckets
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])

    # Merge the buckets
    for i in range(bucketCount):
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    return array

###               <-- Timing -->               ###

# Declaring an array for keeping the number
# of integers to put in X-Axis of the plot
numberOfDatas = []

# Declaring some arrays for keeping the
# times to put in Y-Axis of the plot
countingSortTimes = []
radixSortTimes = []
bucketSortTimes = []

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

    # Counting Sort start time
    startTime = time.time()

    # Doing the Counting Sort
    countingSort(testData)

    # Counting Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    countingSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)

    # Clearing the temporary dataset
    testData.clear()

    # Filling the temporary dataset
    for j in range(numberOfDatas[i]):
        testData.append(dataset[j])

    # Radix Sort start time
    startTime = time.time()

    # Doing the Radix Sort
    radixSort(testData)

    # Radix Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    radixSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)

    # Clearing the temporary dataset
    testData.clear()

    # Filling the temporary dataset
    for j in range(numberOfDatas[i]):
        testData.append(dataset[j])

    # Bucket Sort start time
    startTime = time.time()

    # Doing the Bucket Sort
    bucketSort(testData)

    # Bucket Sort end time
    endTime = time.time()

    # Appending the elapsed time into the list
    bucketSortTimes.append((endTime - startTime) * TIME_MULTIPLIER)

    # Clearing the temporary dataset
    testData.clear()


###               <-- Plotting -->               ###

# Plotting the Counting Sort
plt.plot(numberOfDatas, countingSortTimes, label="Counting Sort")
# Plotting the Radix Sort
plt.plot(numberOfDatas, radixSortTimes, label="Radix Sort")
# Plotting the Bucket Sort
plt.plot(numberOfDatas, bucketSortTimes, label="Bucket Sort")

# Naming the Axises
# Naming the X-Axis
plt.xlabel("Number of Integers")
# Naming the Y-Axis
plt.ylabel("Elapsed time (Milliseconds)")

# Setting a title for the graph
plt.title("Linear Sort Algorithms Comparison")

# Showing a legend on the graph
plt.legend()

# Function to show the graph
plt.show()