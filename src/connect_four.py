import pygame

class Board:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def old_draw(self):
        for row in self.board:
            out_row = ''
            for val in row:
                out_row += '{:2d}'.format(val)
            print(out_row)

    def draw(self):
        surface = pygame.display.get_surface()
        surf_w, surf_h = surface.get_size()
        rect_w, rect_h = (surf_w//self.width), (surf_h//self.height)

        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(surface, [255, 0, 0], [j*surf_w//self.width, i*surf_h//self.height, rect_h, rect_w])
        pygame.display.update()

class Player:
    def __init__(self, name):
        self.name = name

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((700,700))
        pygame.display.set_caption('Connect Four')
        self.running = True
        self.board = Board(7, 6)
        self.players = [Player('Player 1'), Player('Player 2')]
        self.board.old_draw()

    def quit(self):
        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.board.draw()

    def start(self):
        clock = pygame.time.Clock()
        self.draw()
        # Game loop
        while self.running:
            clock.tick(60)
            self.event() # Process events
        pygame.quit()
