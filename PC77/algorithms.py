import random
import time
#
import game_logic as gl

# SORTING ALGORITHMS ------------------------------------------------------- #
def selection_sort(window, settings, background, lines):
    for i in range(len(lines)): 
        min_line = lines[i]
        for j in range(i+1, len(lines)):
            if lines[j].get_height() < min_line.get_height():
                min_line = lines[j]
        swap_lines(lines[i], min_line)
        gl.update_window(window, settings, background, lines)


def bubble_sort(window, settings, background, lines):
    lenght = len(lines)
    for i in range(lenght): 
        for j in range(0, lenght-i-1):  
            if lines[j].get_height() > lines[j+1].get_height(): 
                swap_lines(lines[j], lines[j+1]) 
        gl.update_window(window, settings, background, lines)


# OTHER -------------------------------------------------------------------- #
# mixing lines
def mix_lines(lines):
    for line in lines:
        r = random.randint(0, len(lines) - 1)
        swap_lines(line, lines[r])

        
# swapping two lines
def swap_lines(a, b):
    temp = a.get_height()
    a.set_height(b.get_height())
    b.set_height(temp)