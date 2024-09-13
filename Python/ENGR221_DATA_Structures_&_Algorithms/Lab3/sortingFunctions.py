"""
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> list:
    ### Add your insertionSort implementation here
    for i in range(len(list_to_sort)):
        j = i
        while ( (j > 0) and (list_to_sort[j-1] > list_to_sort[j])):
            tmp = list_to_sort[j]
            list_to_sort[j] = list_to_sort[j-1]
            list_to_sort[j-1] = tmp
            j -= 1
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> list:
    ### Add your bubbleSort implementation here

    for i in range(len(list_to_sort)-1):
        for j in range(len(list_to_sort)-1-i):
            if list_to_sort[j] > list_to_sort[j+1]:
                tmp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j+1]
                list_to_sort[j+1] = tmp
    return list_to_sort

# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':

    print(getRuntime(bubbleSort,100))
    #print(getRuntime(insertionSort,10000))