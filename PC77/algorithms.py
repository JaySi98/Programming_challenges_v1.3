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


def merge_sort(window, settings, arr, l, r):
    if r-l > 1: 
        mid = (r-l)//2 
        #new_l = arr[:mid] # do pozycji mid-1
        #new_r = arr[mid:] # od pozycji mid

        merge_sort(window, settings, arr, l, mid) 
        merge_sort(window, settings, arr, mid, r)  

        k = 0
        i = l
        j = mid
        # Copy data to temp arrays L[] and R[] 
        while i < mid and j < r: 
            if arr[i][0] < arr[j][0]: 
                arr[k] = arr[i] 
                i+= 1
                gl.update_window(window, settings, arr)
            else: 
                arr[k] = arr[j] 
                j+= 1
                gl.update_window(window, settings, arr)
            k+= 1
            time.sleep(settings.sleep_time)

        while i < mid: 
            arr[k] = arr[i] 
            i+= 1
            k+= 1
        
        j = mid
        while j < r: 
            arr[k] = arr[j] 
            j+= 1
            k+= 1


def quick_sort(window, settings, arr, l, r):
    if l < r: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pivot = partition(window, settings,arr, l, r) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(window, settings, arr, l, pivot-1) 
        quick_sort(window, settings, arr, pivot+1, r) 


def heap_sort(window, settings, arr):
    n = len(arr) 
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(window, settings, arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        swap(arr, i, 0) 
        gl.update_window(window, settings, arr)
        #time.sleep(settings.sleep_time)
        heapify(window, settings, arr, i, 0) 

# OTHER -------------------------------------------------------------------- #  
def heapify(window, settings, arr, n, i):
    largest = i  
    l = 2 * i + 1      
    r = 2 * i + 2      

    if l < n and arr[i][0] < arr[l][0]: 
        largest = l 
   
    if r < n and arr[largest][0] < arr[r][0]: 
        largest = r 
  
    if largest != i:  
        swap(arr, i, largest)
        gl.update_window(window, settings, arr)
        time.sleep(settings.sleep_time)
        heapify(window, settings, arr, n, largest) 

# helping function for quick_sort
def partition(window, settings, arr, l, r):
    i = (l-1)         # index of smaller element 
    pivot = arr[r]     # pivot 
  
    for j in range(l, r): 
        # If current element is smaller than the pivot 
        if arr[j][0] < pivot[0]: 
            # increment index of smaller element 
            i = i+1  
            swap(arr, i, j)
            gl.update_window(window, settings, arr)
            time.sleep(settings.sleep_time)

    swap(arr, i+1, r)
    gl.update_window(window, settings, arr) 
    time.sleep(settings.sleep_time)
    return (i+1) 

# creates array of random numbers
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

'''

def merge_sort(window, settings, arr):
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] # do pozycji mid-1
        R = arr[mid:] # od pozycji mid

        merge_sort(window, settings, L) 
        merge_sort(window, settings, R)  

        i = j = k = 0
            
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i][0] < R[j][0]: 
                arr[k] = L[i] 
                i+= 1
                gl.update_window(window, settings, arr)
            else: 
                arr[k] = R[j] 
                j+= 1
                gl.update_window(window, settings, arr)
            k+= 1
            time.sleep(settings.sleep_time)
            

        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
            
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
'''