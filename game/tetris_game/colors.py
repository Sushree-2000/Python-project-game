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


    # cls ~ self for class methods
    @classmethod
    def get_cell_colors(cls):
        return [cls.darkgrey, cls.cyan, cls.blue, cls.yellow, cls.orange, cls.purple, cls.pink, cls.green_aqua, cls.lavender, cls.grey]
