# SETTINGS ----------------------------------------------------------------- #
class Settings():
    def __init__(self):
        # BACKGROUND AND WINDOW 
        # window dimensions
        self.window_dim = (100, 100)
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
        self.line_width = 2
        self.lenght_bounds = (300, 700)
        #colors
        self.colors = [ (255,0,0),
                        (255,0,255),
                        (0,0,255),
                        (0,255,255),
                        (0,255,0),
                        (255,255,0)]

        self.black = (0,0,0)        #background