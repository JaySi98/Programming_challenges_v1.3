import random
#
import game_logic as gl

# SORTING ALGORITHMS ------------------------------------------------------- #
def selection_sort(lines):
    for i in range(len(lines)): 
        min_line = lines[i]
        for j in range(i+1, len(lines)):
            if lines[j].get_height() < min_line.get_height():
                min_line = lines[j]
        swap_lines(lines[i], min_line)


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