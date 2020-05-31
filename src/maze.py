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
        pygame.init()

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
    def __init__(self):
        maze = Maze(4, 4)
        player = Player(0, 0, 1)

    def launch(self):
        pygame.init()
        pygame.display.set_mode((800,800))
        pygame.display.set_caption('Deep Maze')
        self.running = True

    def quit(self):
        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Add other events here
    def update(self):
        pass

    def draw(self):
        pass

    def start(self):
        self.launch() # Initialize game
        # Game loop
        while self.running:
            self.event() # Process events
            self.update() # Update game
            self.draw() # Draw objects
        pygame.quit()
