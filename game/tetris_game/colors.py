class Colors:

    # def get_cell_colors(self):
    grey = (128, 128, 128)
    blue = (0, 0, 255)
    lavender = (230, 230, 250)
    yellow = (255, 255, 0)
    orange = (255, 165, 0)
    purple = (128, 0, 128)
    pink = (255, 192, 203)
    cyan = (0, 255, 255)
    green_aqua = (0, 255, 128)
    darkgrey = (105, 105, 105)
    black = (0, 0, 30)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)


    # cls ~ self for class methods
    @classmethod
    def get_cell_colors(cls):
        return [cls.black, cls.cyan, cls.darkgrey, cls.yellow, cls.orange, cls.blue, cls.pink, cls.green_aqua, cls.lavender, cls.purple]
