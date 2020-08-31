# SETTINGS ----------------------------------------------------------------- #
class Settings():
    def __init__(self):
        # BACKGROUND AND WINDOW 
        # window dimensions
        self.window_dim = (1200, 600)
        self.window_caption = 'Sorting Algorithms Visualization'

        # ALGORITHMS
        self.alg_list = ['selection_sort',
                        'bubble_sort']
        
        # ARRAY
        self.arr_len = 600