# SETTINGS ----------------------------------------------------------------- #
class Settings():
    def __init__(self):
        # BACKGROUND AND WINDOW 
        # window dimensions
        self.window_dim = (1200, 600)
        self.window_caption = 'Sorting Algorithms Visualization'

        # ALGORITHMS
        self.alg_list = ['selection_sort',
                        'bubble_sort',
                        'insertion_sort']
        
        # ARRAY
        self.arr_len = 600
        #colors
        self.black = (0,0,0)#pygame.Color("black")
        self.white = (255,255,255)#pygame.Color("white")
        self.red = (255,0,0)#pygame.Color("red")
        self.green = (0,255,0)#pygame.Color("green")