#program_1
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 50

# Function call
result = linear_search(arr, x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)

n = [10, 20, 50, 100, 200, 500, 1000]
time = [0.0001, 0.0003, 0.0008, 0.0015, 0.0030, 0.0075, 0.0150]

plt.plot(n, time)
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken')
plt.title('Time Complexity of Linear Search')
plt.show()


#program_2

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

import matplotlib.pyplot as plt

# X-axis for time complexity
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Y-axis values for time complexity
Y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Plot the graph
plt.plot(X, Y)
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity (n^2)')
plt.title('Time Complexity Graph of Binary Search')
plt.show()

#program_3

import matplotlib.pyplot as plt

# Function to do insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example sorted array for plotting time complexity
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Plotting the Time Complexity of Insertion Sort
x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.0, 0.1, 0.3, 0.5, 0.7, 1.0, 1.3, 1.5, 1.8]

plt.plot(x, y)
plt.xlabel('Size of array')
plt.ylabel('Time Complexity')
plt.title('Time Complexity of Insertion Sort')
plt.show()


#program_4

import timeit
import random
import matplotlib.pyplot as plt

# Heapify function to maintain the heap property
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Heap Sort function
def heapSort(arr):
    n = len(arr)
    # Build a max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Test data and timing setup
list_lengths = [10000, 20000, 30000, 50000, 60000]
time_taken = []

# Loop to measure the time taken for different list sizes
for length in list_lengths:
    # Generate a random list of the current length
    arr = [random.randint(1, 100000) for _ in range(length)]

    # Measure the time taken to sort the list using heapSort
    setup_code = "from __main__ import heapSort"
    test_code = f"heapSort({arr})"

    # Measure the execution time
    execution_time = timeit.timeit(test_code, setup=setup_code, number=1)
    time_taken.append(execution_time)

# Plotting the results
plt.plot(list_lengths, time_taken)
plt.xlabel('Size of array')
plt.ylabel('Time taken (seconds)')
plt.title('Time Complexity of Heap Sort')
plt.show()
