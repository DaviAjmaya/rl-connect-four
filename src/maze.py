import pygame

class Maze:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.generate()

    def generate(self):
        self.board = [[0 for _ in range(self.height)] for _ in range(self.width)]

    def draw(self):
        for row in self.board:
            out_row = ''
            for val in row:
                out_row += '{:2d}'.format(val)
            print(out_row)

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, dir):
        if dir not in ['up', 'right', 'down', 'left']:
            raise Exception('Illegal move')
        if dir == 'up':
            self.y -= self.speed
        elif dir == 'right':
            self.x += self.speed
        elif dir == 'down':
            self.y += self.speed
        elif dir == 'left':
            self.x -= self.speed

class Game:
