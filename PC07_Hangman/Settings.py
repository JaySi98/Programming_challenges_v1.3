# SETTINGS ----------------------------------------------------------------- #
class Settings():
    def __init__(self):
        # OTHERS ----------------------------------------------------------- #
        # screen dimensions
        self.screen_dim = (1000, 700)
        # background path
        self.background_path = "resources/back.bmp"

        # BUTTONS ---------------------------------------------------------- #
        # buttons width
        self.button_width = 60
        # number of letters that can be placed using loop
        self.buttons_num = 24
        self.buttons_chars = 'abcdefghijklmnopqrstuvwxyz'
        #starting position for placing rects
        self.button_spos = (506, 214)

        # ANSWERS ---------------------------------------------------------- #
        self.answers_size = 1525

        # HANGMAN ---------------------------------------------------------- #
        #number of pieces / lives
        self.pieces_num = 10
        # hangman sprites paths
        self.piece_path = [ "resources/base.bmp",
                            "resources/vertical.bmp",
                            "resources/horizontal.bmp",
                            "resources/rope.bmp",
                            "resources/head.bmp",
                            "resources/body.bmp",
                            "resources/left_arm.bmp",
                            "resources/right_arm.bmp",
                            "resources/left_leg.bmp",
                            "resources/right_leg.bmp" ]
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