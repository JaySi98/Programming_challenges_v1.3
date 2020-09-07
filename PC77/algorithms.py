import random
import time
import math
#
import game_logic as gl

# SORTING ALGORITHMS ------------------------------------------------------- #
def selection_sort(window, settings, arr):
    for i in range(len(arr)): 
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j][0] < arr[lowest][0]:                
                lowest = j
        swap(arr, i, lowest)
        gl.update_window(window, settings, arr)
        time.sleep(settings.sleep_time)


def bubble_sort(window, settings, arr):
    lenght = len(arr)
    for i in range(lenght): 
        for j in range(0, lenght-i-1):  
            if arr[j][0] > arr[j+1][0]: 
                swap(arr, j, j+1) 
                gl.update_window(window, settings, arr)


def insertion_sort(window, settings, arr):
    for i in range(1, len(arr)):
        value = arr[i]
        position = i - 1
        while position >= 0 and value[0] < arr[position][0]:
            arr[position + 1] = arr[position] 
            position -= 1
        arr[position + 1] = value 
        gl.update_window(window, settings, arr)
        time.sleep(settings.sleep_time)


# OTHER -------------------------------------------------------------------- #       
def mix(window, settings, arr):
    for i in range(len(arr)):
        num = random.randint(0,len(arr)-1)
        swap(arr, i, num)
        gl.update_window(window, settings, arr)
    
# swapping two lines
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

