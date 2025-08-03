import pygame
class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.colors = self.get_cell_colors()

    def printGrid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[i][j], end = " ")
            print()

    def get_cell_colors(self):
        grey = (128, 128, 128)
        blue = (0, 0, 255)
        lavender = (230, 230, 250)
        yellow = (255, 255, 0)
        orange = (255, 165, 0)
        purple = (128, 0, 128)
        pink = (255, 192, 203)
        cyan = (0, 255, 255)
        green_aqua = (0, 255, 128)

        grey = (128, 128, 128)
        return [cyan, blue, yellow, orange, purple, pink, green_aqua, lavender, grey]
    
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1) # pygame.Rect(x, y, w, h): (col, row, width, height)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)