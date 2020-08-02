# SETTINGS ----------------------------------------------------------------- #
class Settings():
    def __init__(self):
        #number of pieces / lives
        self.number_pieces = 10

        #screen settings
        self.screen_dim = (1000, 700)
        # background path
        self.background_path = "textures/back.bmp"
        
        # hangman sprites paths
        self.piece_path = [ "textures/base.bmp",
                            "textures/vertical.bmp",
                            "textures/horizontal.bmp",
                            "textures/rope.bmp",
                            "textures/head.bmp",
                            "textures/body.bmp",
                            "textures/left_arm.bmp",
                            "textures/right_arm.bmp",
                            "textures/left_leg.bmp",
                            "textures/right_leg.bmp" ]
        # hangman sprites positions
        self.piece_position = [ [13,614],
                                [45,159],
                                [111,175],
                                [278,223],
                                [252,266],
                                [239,317],
                                [207,336],
                                [325,334],
                                [244,511],
                                [285,511] ]
        