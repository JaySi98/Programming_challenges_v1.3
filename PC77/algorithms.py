import random
import time
#
import game_logic as gl

# SORTING ALGORITHMS ------------------------------------------------------- #
def selection_sort(window, settings, arr):
    for i in range(len(arr)): 
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest]:                
                lowest = j
        swap(arr, i, lowest)
        gl.update_window(window, settings, arr)


def bubble_sort(window, settings, arr):
    lenght = len(arr)
    for i in range(lenght): 
        for j in range(0, lenght-i-1):  
            if arr[j] > arr[j+1]: 
                swap(arr, j, j+1) 
                gl.update_window(window, settings, arr)


def insertion_sort(window, settings, arr):
    for i in range(1, len(arr)):
        value = arr[i]
        position = i - 1
        while position >= 0 and value < arr[position]:
            arr[position + 1] = arr[position] 
            position -= 1
        arr[position + 1] = value 
        gl.update_window(window, settings, arr)


# OTHER -------------------------------------------------------------------- #        
# swapping two lines
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp