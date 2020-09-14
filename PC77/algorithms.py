import random
import time
import math
#
import game_logic as gl

# SORTING ALGORITHMS ------------------------------------------------------- #
#SELECTION_SORT
def selection_sort(window, settings, arr):
    for i in range(len(arr)): 
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j][0] < arr[lowest][0]:                
                lowest = j
        swap(arr, i, lowest)
        gl.update_window(window, settings, arr)
        time.sleep(settings.sleep_time)


# BUBBLE_SORT
def bubble_sort(window, settings, arr):
    lenght = len(arr)
    for i in range(lenght): 
        for j in range(0, lenght-i-1):  
            if arr[j][0] > arr[j+1][0]: 
                swap(arr, j, j+1) 
                gl.update_window(window, settings, arr)


# INSERTION_SORT
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


# QUICK_SORT
def quick_sort(window, settings, arr, l, r):
    if l < r: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pivot = partition(window, settings,arr, l, r) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(window, settings, arr, l, pivot-1) 
        quick_sort(window, settings, arr, pivot+1, r) 


# HEAP_SORT
def heap_sort(window, settings, arr):
    n = len(arr) 
    for i in range(n//2 - 1, -1, -1): 
        heapify(window, settings, arr, n, i) 
   
    for i in range(n-1, 0, -1): 
        swap(arr, i, 0) 
        gl.update_window(window, settings, arr)
        heapify(window, settings, arr, i, 0) 


def radix_sort(window, settings, arr):
    maximum = find_max(arr) 
  
    exp = 1
    while maximum//exp > 0: 
        counting(window, settings, arr, exp) 
        exp *= 10


def shell_sort(window, settings, arr):
    n = len(arr) 
    gap = n//2
  
    while gap > 0: 
  
        for i in range(gap,n):  
            temp = arr[i] 
 
            j = i 
            while  j >= gap and arr[j-gap][0] > temp[0]: 
                arr[j] = arr[j-gap] 
                j -= gap 
                gl.update_window(window, settings, arr)
                time.sleep(settings.sleep_time)
   
            arr[j] = temp 
        gap //= 2


def comb_sort(window, settings, arr):
    n = len(arr) 
    gap = n 
    swapped = True

    while gap !=1 or swapped == 1: 
        gap = get_gap(gap) 
  
        # Initialize swapped as false so that we can 
        # check if swap happened or not 
        swapped = False
  
        # Compare all elements with current gap 
        for i in range(0, n-gap): 
            if arr[i][0] > arr[i + gap][0]: 
                #arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swap(arr, i, i+gap) 
                swapped = True
                gl.update_window(window, settings, arr)
                time.sleep(settings.sleep_time)


def cocktail_sort(window, settings, arr):
    n = len(arr) 
    swapped = True
    start = 0
    end = n-1
    while (swapped == True): 
        # reset the swapped flag on entering the loop, 
        # because it might be true from a previous 
        # iteration. 
        swapped = False
  
        # loop from left to right same as the bubble 
        # sort 
        for i in range (start, end): 
            if (arr[i][0] > arr[i + 1][0]) : 
                #a[i], a[i + 1]= a[i + 1], a[i] 
                swap(arr, i, i+1)
                swapped = True
                gl.update_window(window, settings, arr)
                #time.sleep(settings.sleep_time)
  
        # if nothing moved, then array is sorted. 
        if (swapped == False): 
            break
  
        # otherwise, reset the swapped flag so that it 
        # can be used in the next stage 
        swapped = False
  
        # move the end point back by one, because 
        # item at the end is in its rightful spot 
        end = end-1
  
        # from right to left, doing the same 
        # comparison as in the previous stage 
        for i in range(end-1, start-1, -1): 
            if (arr[i][0] > arr[i + 1][0]): 
                #a[i], a[i + 1] = a[i + 1], a[i] 
                swap(arr, i, i+1)
                swapped = True
                gl.update_window(window, settings, arr)
                #time.sleep(settings.sleep_time)
  
        # increase the starting point, because 
        # the last stage would have moved the next 
        # smallest number to its rightful spot. 
        start = start + 1


# OTHER -------------------------------------------------------------------- #
def get_gap(gap): 
    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return int(gap) 

def find_max(arr):
    maximum = arr[0][0]
    for i in range(len(arr)):
        if arr[i][0] > maximum:
            maximum = arr[i][0]
    return maximum

def find_min(arr):
    minimum = arr[0][0]
    for i in range(len(arr)):
        if arr[i][0] < minimum:
            minimum = arr[i][0]
    return minimum

def counting(window, settings, arr, exp):
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (10) 
     
    for i in range(0, n): 
        index = (arr[i][0] // exp) 
        count[(index) % 10] += 1
   
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        index = (arr[i][0] // exp) 
        output[ count[(index) % 10] - 1] = arr[i] 
        count[(index)%10] -= 1
        i -= 1
   
    i = 0
    for i in range(len(arr)): 
        arr[i] = output[i] 
        gl.update_window(window, settings, arr)
        time.sleep(settings.sleep_time)

# helping function for heap_sort
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
    i = (l-1)         
    pivot = arr[r]     
  
    for j in range(l, r): 
         
        if arr[j][0] < pivot[0]: 
             
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