import pygame

class Board:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def console_draw(self):
        for row in self.board:
            out_row = ''
            for val in row:
                out_row += '{:2d}'.format(val)
            print(out_row)

    def add_circle(self, pos, value):
        if pos < 0 or pos > self.width:
            raise ValueError("Invalid position")

        x, y = 0, pos
        if self.board[x][y] != 0: # If column already full
            return
        while x < self.height-1 and self.board[x+1][y] == 0:
            x += 1
        print(x)
        self.board[x][y] = value

    def draw(self):
        surface = pygame.display.get_surface()
        surf_w, surf_h = surface.get_size()
        rect_w, rect_h = (surf_w//self.width), (surf_h//self.height)
        rad = min(rect_w, rect_h)//2
        rad-= rad//10

        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0: # Empty circles
                    pygame.draw.circle(surface, [255, 255, 255], [j*rect_w+rect_w//2, i*rect_h+rect_h//2], rad)
                if self.board[i][j] == 1:
                    pygame.draw.circle(surface, [255, 0, 0], [j*rect_w+rect_w//2, i*rect_h+rect_h//2], rad)

class Player:
    def __init__(self, name):
        self.name = name

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((700,600))
        self.surface.fill((30,144,255))
        pygame.display.set_caption('Connect Four')
        self.running = True
        self.board = Board(7, 6)
        self.players = [Player('Player 1'), Player('Player 2')]
        self.board.console_draw()

    def quit(self):
        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, _ = pygame.mouse.get_pos()
                self.board.add_circle(pos_x//(self.surface.get_size()[0]//self.board.width), 1)
                self.draw()

    def update(self):
        pass

    def draw(self):
        self.board.draw()
        pygame.display.update()

    def start(self):
        clock = pygame.time.Clock()
        self.draw()
        # Game loop
        while self.running:
            clock.tick(60)
            self.event() # Process events
        pygame.quit()
