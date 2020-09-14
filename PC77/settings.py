# SETTINGS ----------------------------------------------------------------- #
class Settings():
    def __init__(self):
        # BACKGROUND AND WINDOW 
        # window dimensions
        self.window_dim = (1000, 500)
        self.window_caption = 'Sorting Algorithms Visualization'
        
        # ALGORITHMS
        self.alg_list = ['selection_sort',
                         'bubble_sort',
                         'insertion_sort',
                         'quick_sort',
                         'heap_sort',
                         'radix_sort']
        # delay 
        self.sleep_time = 0.01

        # ARRAY
        self.color_lenght = 1500
        self.lenght = 500
        self.line_width = 2
        #background's color
        self.black = (0,0,0)        