import random
import time
#
import game_logic as gl

# SORTING ALGORITHMS ------------------------------------------------------- #
def selection_sort(window, settings, arr):
    for i in range(len(arr)): 
        min_ = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_:
                min_ = arr[j]
        swap(arr[i], min_)
        gl.update_window(window, settings, arr)


def bubble_sort(window, settings, arr):
    lenght = len(arr)
    for i in range(lenght): 
        for j in range(0, lenght-i-1):  
            if arr[j] > arr[j+1]: 
                swap(arr[j], arr[j+1]) 
        gl.update_window(window, settings, arr)


# OTHER -------------------------------------------------------------------- #
# mixing lines
def mix_lines(lines):
    for line in lines:
        r = random.randint(0, len(lines) - 1)
        swap_lines(line, lines[r])

        
# swapping two lines
def swap(a, b):
    temp = a
    a = b
    b = temp